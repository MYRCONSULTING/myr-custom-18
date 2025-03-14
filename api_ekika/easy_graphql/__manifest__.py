# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'GraphQL API for Odoo',
    'summary': """This module enables precise API responses by defining query parameters that specify which data should be included in the response.
        GraphQL API
        Odoo API GraphQL
        GraphQL module for Odoo
        Query Language
        GraphQL Integration Odoo
        API Data Fetching
        Query-based API Odoo
        Odoo API customization
        GraphQL data filtering Odoo
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Productivity,Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'api_framework_base', 'api_auth_apikey'],
    'external_dependencies': {
        'python': ['graphql-core==3.2.3'],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/easy_api.xml',
        'documentation/easy_graphql_doc.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'easy_graphql/static/src/scss/graphql_doc.scss'
        ]
    },
    'images': ['static/description/banner.png'],
    'price': 0.25,
    'currency': 'EUR',
    'description': """
    """
}
