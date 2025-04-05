# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management System',

    'depends': ['base'],
    'author': 'Ishmam Khan',
    'category': 'Hospital',
    'version': '76.0',
    'summary': 'Manage patients',
    'description': 'A module to manage patients in Odoo',
    'depends': [
        'mail',
        'product',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_view.xml',
        'views/appointment_views.xml',
        'views/appointment_line_views.xml',
        'views/patient_tag_view.xml',
        'views/account_move_views.xml',
        'views/menu.xml',
        'views/patient_action.xml',


    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
