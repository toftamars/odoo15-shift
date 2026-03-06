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
