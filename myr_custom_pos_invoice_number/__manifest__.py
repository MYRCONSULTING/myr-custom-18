# -*- coding: utf-8 -*-
{
    "name": "myr_custom_pos_invoice_number",
    'version': '1.0',
    'author': 'myr',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'summary': 'myr_custom_pos_invoice_number',
    'description': """
- Odoo Invoice number on pos receipt
    """,
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'myr_custom_pos_invoice_number/static/src/js/pos_store.js',
            'myr_custom_pos_invoice_number/static/src/xml/**/*',
        ],
    },
    'price': 0.0,
    'currency': "EUR",
    'application': True,
    'installable': True,
    "license": "LGPL-3",
    
    
}
