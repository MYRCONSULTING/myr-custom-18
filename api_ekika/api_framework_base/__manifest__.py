# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

{
    'name': 'REST API Foundation',
    'company': 'EKIKA CORPORATION PRIVATE LIMITED',
    'author': 'EKIKA',
    'apimeta': {
        'author': 'Anand Shukla (EKIKA)',
        'email': 'hello@ekika.co'
    },
    'apidoc': 'https://ekika.co/odoo/apps/api_framework_base/16/doc',
    'website': 'https://ekika.co',
    'category': 'Tools',
    'version': '18.0.1.0',
    'license': 'OPL-1',
    'depends': ['base', 'web', 'mail', 'ekika_utils', 'ekika_widgets'],
    'data': [
        'security/groups.xml',
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'views/easy_api.xml',
        'views/res_config_settings_views.xml',
        'views/menus.xml',
    ],
    'demo': [
        'data/api_framework_base_demo.xml',
    ],
    'live_test_url': 'https://youtu.be/gxGNctBO028?si=jiJpxiwIWLfZUF4e',
    'assets': {},
    'images': ['static/description/banner.gif'],
    'price': 61.25,
    'currency': 'EUR',
    'description': """
    """,
    'summary': """Odoo REST API Framework allows you all api related activity around odoo.
Find more details inside the app details. It allows possibilities around all following:
Odoo API Odoo REST API Odoo API authentication Odoo OAuth2 integration Odoo API key management
Odoo basic authentication API Odoo API framework Odoo GraphQL Odoo JSON API Odoo custom API
Odoo third-party API integration Odoo API module Odoo API for mobile apps Odoo external API access
Odoo dynamic API Odoo API webhooks Odoo API for ERP systems Odoo API for ecommerce Odoo API documentation
Odoo API for data synchronization Odoo API for reporting Odoo API versioning Odoo API and microservices
Odoo API performance optimization Odoo API for SaaS applications Odoo API and database access Odoo API connectors
Odoo API for CRM Odoo API for inventory management Odoo API for accounting integration General API Terms Odoo API
Odoo APIs Odoo API integration Odoo API module Odoo API connector Odoo API framework Odoo API documentation
Odoo API reference Odoo API examples Odoo API tutorials Authentication and Authorization Odoo API authentication
Odoo API auth Odoo OAuth2 Odoo OAuth2 integration Odoo API OAuth2 Odoo API key Odoo API key management
Odoo API authentication methods Odoo basic auth API Odoo API JWT Odoo API security Odoo API SSL Odoo API token
Odoo API bearer token API Types and Protocols Odoo REST API Odoo RESTful API Odoo JSON-RPC Odoo XML-RPC Odoo GraphQL
Odoo SOAP API Odoo gRPC API Odoo Web API Odoo HTTP API Odoo API endpoints Odoo API methods Specific API Functionalities
Odoo API for CRM Odoo API for ERP Odoo API for ecommerce Odoo API for accounting Odoo API for inventory Odoo API for sales
Odoo API for purchase Odoo API for manufacturing Odoo API for HR Odoo API for project management Odoo API for marketing
Odoo API for website Odoo API for POS Integration and Connectivity Odoo API integration Odoo third-party API integration
Odoo API with Shopify Odoo API with Magento Odoo API with Salesforce Odoo API with Google Odoo API with Facebook
Odoo API with Amazon Odoo API with QuickBooks Odoo API with Mailchimp Odoo API with Zapier Odoo API with Slack
Odoo API with Twilio API Development and Customization Odoo custom API Odoo API development Odoo API customization
Odoo API extension Odoo API builder Odoo API SDK Odoo API tools Odoo API generator Odoo API testing Odoo API debugging
Odoo API sandbox Odoo API developer tools Data Management and Synchronization Odoo API for data synchronization
Odoo API data import Odoo API data export Odoo API data migration Odoo API for bulk operations Odoo API for data integration
Odoo API ETL Odoo API data mapping API Performance and Optimization Odoo API performance Odoo API optimization
Odoo API caching Odoo API rate limiting Odoo API scalability Odoo API load balancing Odoo API latency Odoo API throughput
API Security and Compliance Odoo API security Odoo API encryption Odoo API compliance Odoo API GDPR Odoo API data protection
Odoo API access control Odoo API permissions Odoo API roles Odoo API auditing API Monitoring and Analytics Odoo API monitoring
Odoo API analytics Odoo API logging Odoo API metrics Odoo API usage statistics Odoo API error tracking
Odoo API performance monitoring API Versioning and Updates Odoo API versioning Odoo API updates Odoo API changelog
Odoo API backward compatibility Odoo API deprecation API Use Cases and Examples Odoo API use cases Odoo API examples
Odoo API case studies Odoo API real-world applications Odoo API best practices GraphQL and Advanced APIs Odoo GraphQL API
Odoo GraphQL integration Odoo advanced API Odoo API extensions Odoo API enhancements API Frameworks and Libraries
Odoo API frameworks Odoo API libraries Odoo API SDKs Odoo API client libraries Odoo API wrappers API Marketplace and Modules
Odoo API apps Odoo API marketplace Odoo API modules Odoo API addons Odoo API plugins API Support and Community
Odoo API support Odoo API forums Odoo API community Odoo API help Odoo API tutorials Odoo API guides
API for Mobile and Frontend Development Odoo API for mobile apps Odoo API for iOS Odoo API for Android Odoo API for frontend
Odoo API for React Odoo API for Angular Odoo API for Vue.js API Documentation and Resources Odoo API docs
Odoo API documentation Odoo API reference Odoo API guides Odoo API tutorials Odoo API examples Odoo API samples
Odoo API wiki API Automation and Workflow  Odoo API automation Odoo API workflows Odoo API scripting Odoo API bots
Odoo API triggers Miscellaneous API Terms Odoo API connectors Odoo API webhooks Odoo API triggers Odoo API events
Odoo API subscriptions Odoo API billing Odoo API pricing Odoo API trial Odoo API free Odoo API premium
API Testing and Quality Assurance Odoo API testing Odoo API QA Odoo API test tools Odoo API test cases Odoo API validation
API Error Handling and Debugging Odoo API error handling Odoo API debugging Odoo API error codes Odoo API troubleshooting
Odoo API issue resolution API Best Practices and Standards Odoo API best practices Odoo API standards Odoo API guidelines
Odoo API design patterns Odoo API architecture API Licensing and Pricing Odoo API licensing Odoo API pricing
Odoo API subscription Odoo API cost Odoo API free trial Odoo API plans API Integration Tools and Platforms Odoo API Zapier
Odoo API Integromat (Make) Odoo API MuleSoft Odoo API Dell Boomi Odoo API Tray.io Odoo API Workato
API Maintenance and Support Odoo API maintenance Odoo API support services Odoo API managed services Odoo API consulting
Odoo API professional services API Compliance and Legal Odoo API GDPR compliance Odoo API data privacy Odoo API legal
Odoo API terms of service Odoo API SLA API Compatibility and Requirements Odoo API compatibility Odoo API requirements
Odoo API prerequisites Odoo API supported versions Odoo API system requirements API Integration Scenarios
Odoo API ERP integration Odoo API CRM integration Odoo API ecommerce integration Odoo API HR integration
Odoo API finance integration Odoo API marketing integration API Use in Specific Industries Odoo API for healthcare
Odoo API for education Odoo API for manufacturing Odoo API for retail API App Builder Odoo Studio API Odoo Experience
Odoo Flutter Runbot, crm, inventory, saas, API Odoo Login API Odoo Free API Odoo mobile Odoo react Odoo app store apps odoo
download odoo files odoo pos api odoo software api odoo website api odoo crm api odoo community api odoo enterprise api
odoo inventory odoo online api odoo external api odoo external api login odoo app builder Odoo module, oca odoo supported api
shopify odoo supported api github odoo supported api third party apps erp appstore dashboard amazon api woocommerce
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

