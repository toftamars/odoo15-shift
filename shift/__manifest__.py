# -*- coding: utf-8 -*-
{
    'name': 'Shift',
    'version': '1.0',
    'category': 'Human Resources/Shift',
    'summary': 'Vardiya planlaması ve çalışan ataması',
    'description': """
Shift Modülü
============

Bu modül Odoo 15 için vardiya planlaması yapar:
- Vardiya şablonları (Sabah, Öğle, Gece vb.)
- Haftalık/aylık vardiya planları
- Çalışan-vardiya atamaları
- Analitik hesaplar ile entegrasyon
- Sadece iç kullanıcılar ile çalışır
    """,
    'author': 'Shift',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base', 'hr', 'analytic'],
    'data': [
        'security/shift_security.xml',
        'security/ir.model.access.csv',
        'data/shift_template_data.xml',
        'views/account_analytic_account_views.xml',
        'views/shift_template_views.xml',
        'views/shift_schedule_views.xml',
        'views/shift_assignment_views.xml',
        'views/shift_actions.xml',
        'views/shift_menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
