# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'API Log File Access',
    'summary': """The api_log module provides comprehensive logging for API interactions, offering real-time tracking of API activities within Odoo.
        API Log
        Odoo API Log
        API Management Odoo
        Real-Time Log Viewer
        API Log Viewer
        Odoo API Debugging
        API Monitoring Odoo
        API activity tracking
        Real-time API logs Odoo
        Odoo API monitoring
        API interaction logs
        Odoo API audit
        Track API activities Odoo
        Odoo REST API logging
        API logs module Odoo
        Odoo API request tracking
    """,
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'api_framework_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/easy_api.xml',
        'wizard/api_log.xml',
    ],
    'assets': {},
    'images': ['static/description/banner.png'],
    'price': 0.01,
    'currency': 'EUR',
    'description': """
    """
}
