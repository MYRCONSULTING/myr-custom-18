# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'Json API v1.1 for Odoo',
    'summary': """This module JSON API for Odoo provides a structured approach to JSON requests and responses, simplifying API development.
        JSON API
        JSON API for Odoo
        Odoo JSON API
        JSON API module Odoo
        Structured API Odoo
        Odoo API development
        API Specification
        JSON API Integration Odoo
        JSON API Requests Odoo
        Fetch and Modify Resources
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Extra Tools,Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'api_framework_base', 'api_auth_apikey'],
    'data': [
        'security/ir.model.access.csv',
        'views/easy_api.xml',
        'documentations/easy_jsonapi_doc.xml',
        'wizard/jsonapi_trial_wizard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'easy_jsonapi/static/src/scss/jsonapi_doc.scss',
        ]
    },
    'images': ['static/description/banner.png'],
    'price': 0.25,
    'currency': 'EUR',
    'description': """
    """
}
