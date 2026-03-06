# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    user_ids = fields.Many2many(
        'res.users',
        'analytic_account_user_rel',
        'account_id',
        'user_id',
        string='İç Kullanıcılar',
        domain=[('share', '=', False)],
        help='Bu analitik hesaba atanmış iç kullanıcılar'
    )
