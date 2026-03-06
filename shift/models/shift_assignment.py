# -*- coding: utf-8 -*-

from datetime import datetime, time, timedelta

from odoo import api, fields, models


class ShiftAssignment(models.Model):
    _name = 'shift.assignment'
    _description = 'Vardiya Ataması'
    _rec_name = 'display_name'

    display_name = fields.Char(compute='_compute_display_name', string='Görünen Ad')

    schedule_id = fields.Many2one(
        'shift.schedule',
        string='Vardiya Planı',
        required=True,
        ondelete='cascade'
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Çalışan',
        required=True
    )
    template_id = fields.Many2one(
        'shift.template',
        string='Vardiya Şablonu',
        required=True
    )
    assignment_date = fields.Date(string='Atama Tarihi', required=True)
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analitik Hesap',
        help='Bu atama için maliyet analizi yapılacak analitik hesap'
    )
    date_start = fields.Datetime(
        string='Başlangıç',
        compute='_compute_calendar_dates',
        store=True
    )
    date_stop = fields.Datetime(
        string='Bitiş',
        compute='_compute_calendar_dates',
        store=True
    )
    color = fields.Integer(related='template_id.color', string='Renk')

    @api.depends('employee_id', 'template_id', 'assignment_date')
    def _compute_display_name(self):
        for rec in self:
            if rec.employee_id and rec.template_id:
                rec.display_name = f"{rec.employee_id.name} - {rec.template_id.name} ({rec.assignment_date})"
            else:
                rec.display_name = 'Yeni Atama'

    @api.depends('assignment_date', 'template_id', 'template_id.start_time', 'template_id.end_time')
    def _compute_calendar_dates(self):
        for rec in self:
            if rec.assignment_date and rec.template_id:
                start_h = int(rec.template_id.start_time)
                start_m = int((rec.template_id.start_time % 1) * 60)
                end_h = int(rec.template_id.end_time)
                end_m = int((rec.template_id.end_time % 1) * 60)
                rec.date_start = datetime.combine(
                    rec.assignment_date,
                    time(start_h, start_m)
                )
                end_dt = datetime.combine(
                    rec.assignment_date,
                    time(end_h, end_m)
                )
                if rec.template_id.end_time <= rec.template_id.start_time:
                    end_dt += timedelta(days=1)
                rec.date_stop = end_dt
            else:
                rec.date_start = False
                rec.date_stop = False

    @api.onchange('template_id')
    def _onchange_template_analytic(self):
        """Şablondan analitik hesabı taşı"""
        if self.template_id and self.template_id.analytic_account_id:
            self.analytic_account_id = self.template_id.analytic_account_id

    @api.onchange('schedule_id')
    def _onchange_schedule_analytic(self):
        """Plandan analitik hesabı taşı"""
        if self.schedule_id and self.schedule_id.analytic_account_id:
            self.analytic_account_id = self.schedule_id.analytic_account_id
