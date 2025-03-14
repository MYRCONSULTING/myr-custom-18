# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'API Key Based Authentication',
    'summary': """API Key Authentication secures your API endpoints by requiring clients to include an API Key in the request headers.
        API Key Authentication
        Odoo API Authentication
        API Security
        Authentication for APIs
        x-api-key Header
        Authorized API Access
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Productivity,Extra Tools,Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'api_framework_base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter_data.xml',
        'views/api_auth_apikey.xml',
        'views/easy_api.xml',
        'views/menus.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {},
    'images': ['static/description/banner.png'],
    'price': 0.01,
    'currency': 'EUR',
    'description': """
    """
}

