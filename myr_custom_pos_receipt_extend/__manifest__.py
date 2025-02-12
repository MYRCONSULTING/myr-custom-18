# -*- coding: utf-8 -*-
{
    'name': "myr_custom_pos_receipt_extend",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "summary": "myr_custom_pos_receipt_extend",
    "description": """myr_custom_pos_receipt_extend""",
    'author': '',
    'website': "https://www.myrconsulting.net",
    'company': '',
    'maintainer': '',
    'depends': ['point_of_sale', 'sale'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'myr_custom_pos_receipt_extend/static/src/xml/OrderReceipt.xml',
            'myr_custom_pos_receipt_extend/static/src/js/PosOrder.js',
        ]
    },
    
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
