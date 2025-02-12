{
    'name': "myr_custom_download_invoice",
    'summary': "",

    'description': """


Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'author': "myr",
    'website': "http://myrconsulting.net/",
    'support': "martha.laurente@gmail.com",
    'sequence': 24,
    'category': 'Sales/Point of Sale',
    'version': '1.0',
    'depends': ['point_of_sale'],

    # always loaded
    'data': {
        'views/res_config_setting_views.xml',
    },
    'assets': {
        'point_of_sale._assets_pos': [
            'myr_custom_download_invoice/static/src/**/*',
        ],
    },
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
