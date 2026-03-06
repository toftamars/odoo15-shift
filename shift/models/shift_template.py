# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ShiftTemplate(models.Model):
    _name = 'shift.template'
    _description = 'Vardiya Şablonu'

    name = fields.Char(string='Vardiya Adı', required=True)
    start_time = fields.Float(string='Başlangıç Saati', required=True)
    end_time = fields.Float(string='Bitiş Saati', required=True)
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analitik Hesap',
        help='Bu vardiya için maliyet analizi yapılacak analitik hesap'
    )
    active = fields.Boolean(default=True)
    color = fields.Integer(string='Renk')

    @api.constrains('start_time', 'end_time')
    def _check_times(self):
        for record in self:
            if record.start_time < 0 or record.start_time > 24:
                raise models.ValidationError('Başlangıç saati 0-24 arasında olmalıdır.')
            if record.end_time < 0 or record.end_time > 24:
                raise models.ValidationError('Bitiş saati 0-24 arasında olmalıdır.')
