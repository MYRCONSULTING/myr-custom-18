# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

import json
import traceback
from werkzeug.routing import Map,Rule
from werkzeug.datastructures import Headers
from werkzeug.exceptions import Unauthorized, NotFound
from odoo.addons.api_framework_base.api_dispatcher import EasyAPI
from odoo.http import request, Response
from odoo.tools import json_default
from odoo.exceptions import AccessDenied


class RestJson(EasyAPI):
    api_type = 'rest_json'

    @classmethod
    def confirm_mimetype(cls):
        if request.httprequest.method == 'OPTIONS':
            return True
        return request.httprequest.mimetype in ('application/json')

    def post_init(self):
        super().post_init()
        request.easyapi = dict(
            record=self.api_record,
            error_debug=self.api_record.error_debug,
            error_detail=self.api_record.error_detail,
            pagesize=self.api_record.page_size
        )

    def url_match(self):
        """Identify parameters from URL.

        /res.partner/search_read
        """
        endpoint = request.base_endpoint
        urls = Map([
            Rule(f'/{endpoint}/<string:model>/<string:method>'),
        ]).bind('')
        return urls.match(self.request.httprequest.path)[1]

    def pre_process(self):
        """Prepare the process so it can be easy served by subsequent api."""
        super().pre_process()
        self.request.easyapi.update(self.url_match())

    def process_request(self, endpoint, args):
        """RestJson API Process Invoke Entry"""

        self.request.params = self.request.get_http_params()
        ctx = self.request.params.pop('context', None)
        if ctx is not None and self.request.db:
            self.request.update_context(**ctx)

        if self.request.db:
            result = self.request.registry['ir.http']._dispatch(endpoint)
        else:
            result = endpoint(**self.request.params)
        return self.make_api_response(result)

    def handle_error(self, exc):
        extra_headers = []
        if isinstance(exc, AccessDenied):
            status = 401
            error = {'title': 'Unauthorized', 'detail': exc.args}
        elif isinstance(exc, Unauthorized):
            status = 401
            extra_headers = exc.get_headers()
            error = {'title': 'Unauthorized', 'detail': exc.description}
        elif isinstance(exc, NotFound):
            status = 400
            error = {'title': 'Bad Request', 'detail': exc.description}
        else:
            status = 400
            error = {'title': 'Bad Request', 'detail': exc.args}
        if request.easyapi.get('error_debug'):
            error.update({'debug': traceback.format_exc()})
        if not request.easyapi.get('error_detail'):
            error.pop('detail')
        data = json.dumps(error, ensure_ascii=False, default=json_default)
        headers = Headers()
        headers['Content-Type'] = 'application/json'
        headers.extend(extra_headers)
        return Response(data, headers=headers, status=status)

    def make_api_response(self, result):
        if isinstance(result, Response):
            return result
        data = json.dumps(result, ensure_ascii=False, default=json_default)
        headers = Headers()
        headers['Content-Length'] = len(data)
        headers['Content-Type'] = 'application/json; charset=utf-8'
        return Response(data, headers=headers ,status=200)

