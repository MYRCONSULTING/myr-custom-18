# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo import models
from odoo import http


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _generate_routing_rules(self, modules, converters):
        if not http.request:
            yield from super()._generate_routing_rules(modules, converters)
            return
        else:
            all_rest_json_apis = http.request.env['easy.api'].sudo().search([('api_type', '=', 'rest_json')])
            all_endpoints = [f'/{r.base_endpoint}/<string:model>/<string:method>' for r in all_rest_json_apis]

            for url, endpoint in super()._generate_routing_rules(modules, converters):
                if url in ['/_rest_json_dynamic_api_route']:
                    for url in all_endpoints:
                        yield url, endpoint
                else:
                    yield url, endpoint
