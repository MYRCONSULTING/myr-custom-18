# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'API JWT Authentication',
    'summary': """This module enables JWT-based authentication within the API Framework, ensuring secure access to protected endpoints.
        JWT Authentication
        Odoo API Authentication
        API Security
        Authentication for APIs
        API Security with JWT
        JWT token Odoo
        API Framework JWT
        Token-Based Authentication
        JWT integration Odoo
        API token security Odoo
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Productivity,Extra Tools,Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'api_framework_base'],
    'external_dependencies': {
        'python': ['PyJWT==2.3.0'],
    },
    'data': [
        'views/easy_api.xml'
    ],
    'assets': {},
    'images': ['static/description/banner.png'],
    'price': 0.01,
    'currency': 'EUR',
    'description': """
    """
}
