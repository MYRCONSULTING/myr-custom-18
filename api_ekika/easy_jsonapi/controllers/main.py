# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

"""Test-API Controllers"""

import json
from base64 import b64encode
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.export import ExcelExport


class JsonAPI(ExcelExport, http.Controller):

    @http.route(
        ['/_jsonapi_dynamic_api_route'],
        auth='api',
        csrf=False,
        type='api',
        cors='api',
        methods=['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS']
    )
    def jsonApiGetController(self, **kw):
        return request.env['easy.jsonapi'].serve()

    @http.route('/_jsonapi_dynamic_api_route/export', type='api', cors='api', auth="api")
    def jsonApiExport(self):
        data = request.get_json_data()
        try:
            result = self.base(json.dumps(data))
            result.is_api = False
            result_data = f'{{"file_data": "{b64encode(result.data).decode()}"}}'
            result.data = result_data.encode()
            return result
        except Exception as exc:
            raise exc

    @http.route('/_jsonapi_dynamic_api_route/report', type='api', cors='api', auth="api")
    def jsonApiReport(self):
        values = request.get_json_data()
        if not values.get('converter') and not values.get('report_ref'):
            raise Exception('Provide inputs')
        try:
            converter = values.get('converter')
            report_ref = values.get('report_ref')
            res_ids = values.get('res_ids')
            data = values.get('data')
            ir_report = request.env['ir.actions.report']
            if converter == 'html':
                html = ir_report._render_qweb_html(report_ref, res_ids, data=data)[0]
                result_data = {"file_data": f"{b64encode(html).decode()}"}
                return result_data
            elif converter == 'pdf':
                pdf = ir_report._render_qweb_pdf(report_ref, res_ids, data=data)[0]
                result_data = {"file_data": f"{b64encode(pdf).decode()}"}
                return result_data
            elif converter == 'text':
                text = ir_report._render_qweb_text(report_ref, res_ids, data=data)[0]
                result_data = {"file_data": f"{b64encode(text).decode()}"}
                return result_data
            else:
                raise Exception('Provide valid converter')
        except Exception as exc:
            raise exc
