# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'API framework Access and Permissions',
    'summary': """This module manages access rights, ensuring that only authorized users can access specific API endpoints or resources.
        API Access Control
        Personalized API Access
        Odoo API Access Rights
        Access Rights for APIs
        API Authorization Odoo
        API resource permissions Odoo
        Access rights API Odoo
        Odoo API authorization
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'API Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'ekika_utils','api_framework_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/easy_api.xml',
        'views/api_custom_control.xml',
        'views/custom_model_access.xml',
        'views/menus.xml',
    ],
    'assets': {},
    'images': ['static/description/banner.png'],
    'price': 0.01,
    'currency': 'EUR',
    'description': """
    """
}
