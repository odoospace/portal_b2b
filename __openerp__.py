# -*- coding: utf-8 -*-
{
    'name': "Portal B2B",

    'summary': """
        Portal B2B stuff""",

    'description': """
        Portal B2B
    """,

    'author': "Impulzia",
    'website': "http://www.impulzia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '9.0.2.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'web_readonly_bypass'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}