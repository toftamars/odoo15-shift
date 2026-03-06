# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ShiftAssignment(models.Model):
    _name = 'shift.assignment'
    _description = 'Vardiya Ataması'

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
