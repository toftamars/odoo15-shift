# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ShiftSchedule(models.Model):
    _name = 'shift.schedule'
    _description = 'Vardiya Planı'

    name = fields.Char(string='Plan Adı', required=True)
    date_start = fields.Date(string='Başlangıç Tarihi', required=True)
    date_end = fields.Date(string='Bitiş Tarihi', required=True)
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analitik Hesap',
        help='Bu plan için maliyet analizi yapılacak analitik hesap'
    )
    user_ids = fields.Many2many(
        'res.users',
        'shift_schedule_user_rel',
        'schedule_id',
        'user_id',
        string='İç Kullanıcılar',
        domain="[('share', '=', False)]",
        help='Analitik hesaba ait iç kullanıcılar - önce analitik hesap seçin. Analitik hesaplarda tanımlı kullanıcıları seçin.'
    )
    assignment_ids = fields.One2many(
        'shift.assignment',
        'schedule_id',
        string='Vardiya Atamaları'
    )
    state = fields.Selection([
        ('draft', 'Taslak'),
        ('confirmed', 'Onaylandı'),
        ('done', 'Tamamlandı'),
    ], string='Durum', default='draft', required=True)

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_start > record.date_end:
                raise models.ValidationError('Bitiş tarihi başlangıç tarihinden önce olamaz.')

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_done(self):
        self.write({'state': 'done'})

    @api.onchange('user_ids')
    def _onchange_user_ids(self):
        """Seçilen kullanıcılardan vardiya atamaları oluştur"""
        if self.user_ids and self.analytic_account_id and self.date_start:
            template = self.env['shift.template'].search([('active', '=', True)], limit=1)
            existing_user_ids = self.assignment_ids.mapped('employee_id.user_id').ids
            commands = [(4, a.id) for a in self.assignment_ids]
            for user in self.user_ids:
                if user.id not in existing_user_ids:
                    employee = self.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)
                    if employee and template:
                        commands.append((0, 0, {
                            'employee_id': employee.id,
                            'template_id': template.id,
                            'assignment_date': self.date_start,
                            'analytic_account_id': self.analytic_account_id.id,
                        }))
                        existing_user_ids.append(user.id)
            if len(commands) > len(self.assignment_ids):
                self.assignment_ids = commands
