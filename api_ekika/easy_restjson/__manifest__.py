# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'Odoo Standard RESTful JSON API',
    'summary': """This module integrates Odoo's Standard RESTful JSON formats with API framework features, offering multiple authentication methods, access control, logging, and CORS support.
        Odoo RESTful JSON API
        Odoo Swagger API
        Odoo API with Swagger
        Odoo REST API
        Odoo custom API
        Odoo custom API endpoints
        API Framework Integration
        Odoo API Security
        RESTful API for Odoo
        Odoo API Integration
        API Authentication
        Odoo RESTful API
        Odoo JSON API
        API framework Odoo
        Odoo API authentication
        CORS support Odoo API
        Odoo API access control
        RESTful JSON Odoo
        Odoo API logging module
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Extra Tools,Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'api_framework_base', 'api_auth_apikey'],
    'data': [
        'views/easy_api.xml',
        'views/swagger_templates.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'easy_restjson/static/src/components/style.scss',
            'easy_restjson/static/src/components/easy_restjson_doc.js',
            'easy_restjson/static/src/components/easy_restjson_doc.xml',
        ]
    },
    'images': ['static/description/banner.png'],
    'price': 0.25,
    'currency': 'EUR',
    'description': """
    """
}
