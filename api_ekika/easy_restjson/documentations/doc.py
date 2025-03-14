# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

import json
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError


class SwaggerEasyRestJsonDoc(http.Controller):

    @http.route([
        '/swagger/restjson/<string:api_endpoint>',
        '/swagger/restjson/<int:api_endpoint>'
    ], type='http', auth='user')
    def swagger_easy_restjson_doc(self, api_endpoint, **kwargs):
        if not request.env.user.has_group('api_framework_base.group_api_user_read_only'):
            raise AccessError('You are not authorized to access.')

        if isinstance(api_endpoint, int):
            api_endpoint = request.env['easy.api'].browse(api_endpoint)
        elif isinstance(api_endpoint, str):
            all_found_apis = request.env['easy.api'].search([('base_endpoint', '=', api_endpoint), ('state', '=', 'active')])
            if all_found_apis and len(all_found_apis) == 1:
                api_endpoint = all_found_apis[0]

        swagger_values = request.env['restjson.swagger.doc'].swagger_doc(api_endpoint)
        swagger_json = json.dumps(swagger_values)
        return request.render('easy_restjson.swagger_template', {'swagger_json': swagger_json})
