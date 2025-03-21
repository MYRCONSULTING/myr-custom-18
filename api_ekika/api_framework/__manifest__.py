# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'Odoo RESTful API Framework with JsonAPI, GraphQL and more',
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'website': 'https://ekika.co',
    'category': 'Productivity,Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': [
        'base', 'web', 'ekika_utils', 'api_framework_base', 'api_log',
        'api_auth_apikey','api_auth_apiuser', 'api_auth_basic', 'api_auth_oauth2', 'api_auth_jwt',
        'api_auth_public', 'api_resource_access', 'easy_graphql', 'easy_jsonapi', 'api_cors_config',
        'easy_jsonapi_apikey_signup', 'easy_jsonapi_basic_signup', 'easy_restjson', 'jsonapi_studio',
        'restjson_studio'
    ],
    'demo': [
        'demo/api_framework_demo.xml',
        'demo/api_custom_control_demo.xml',
    ],
    'live_test_url': 'https://youtu.be/gxGNctBO028?si=jiJpxiwIWLfZUF4e',
    'assets': {},
    'images': ['static/description/banner.gif'],
    'price': 1.25,
    'currency': 'EUR',
    'description': """
Advance RESTful API with Security for Odoo. It allows access of resources/data with (optional) predefined JSON:API schema of response Odoo models, fields and much more.
Auto-generated easy to access and secure documentation with Open API (Swagger).
Reach set of Authentication and Authorization available with dynamic configuration control.
Multi-API, Multi-Company & Multi-Website Supported.
Easy to Use and Easy to Secure access of resources.
Free Support
Bug free API with flexible to use in any manner.
Maintain high level of code quality and very easy to extend. Useful for developers.
Free Client libraries are available for Flutter, Android (Java), Python, PHP, C++ on git.
Tags: api, restapi, connector, integration, endpoint, connection, route, routes, access records, call methods, openapi, oauth, webhooks, report, swagger, calling method
    """,
    'summary': """GraphQL, Json:API, OAuth2, API Key, Sudo Authorization, Personalized Access Management and much more.
        Odoo API Authentication
        API Security
        Authentication for APIs
        GraphQL
        JSON API
        OAuth2 Authentication
        Access Managemenet
        API Key Authentication
        User Based Authentication
        API Security with JWT
        API Framework JWT
        Token-Based Authentication
        REST API
        RESTful API for Odoo
        Fully dynamic customizable APIs for Odoo
        Odoo REST API
        ORF - Odoo REST Framework
        External API - Odoo 17.0 documentation
        JSON API
        JSON API Schema
        Open API
        Swagger API
        swagger.io
        ekika.co
        Ekika Corporation Private Limited
        Odoo API
        Odoo Easy API
        Odoo Easy API Freamwork
        Odoo REST API Framework
        Odoo Best API
        Odoo Apps API
        Odoo API Module
        ERP API
        Webhook
        Connection
        Reports
        Reporting
        Inventory Central
        Connector
        Integration
        API Integration
        Various Route
        Routes by Models
        Routes by Operation
        GET, POST, PATCH, DELETE
        Read, Create, Update, Delete
    """
}
