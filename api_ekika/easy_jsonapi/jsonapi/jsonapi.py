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
from werkzeug.exceptions import Unauthorized
from odoo.addons.api_framework_base.api_dispatcher import EasyAPI
from odoo.http import request, Response
from odoo.tools import json_default
from odoo.exceptions import AccessDenied, AccessError, ValidationError
from odoo.addons.ekika_utils.tools.jsonapi_exceptions import (JsonAPIException, AuthorizationFailureException,
                                                              ResourceNotFoundException,
                                                              ValidationError as JsonApiValidationError,
                                                              AuthenticationFailureException,
                                                              BadRequestException,
                                                              UnsupportedMediaTypeException)

from .utils import *



class JsonAPI(EasyAPI):
    api_type = 'jsonapi'

    @classmethod
    def confirm_mimetype(cls):
        if request.httprequest.method == 'OPTIONS':
            return True
        if request.httprequest.accept_mimetypes.best == 'application/vnd.api+json':  # checks Accept
            return True
        elif request.httprequest.mimetype == 'application/vnd.api+json': # checks Content-Type
            return True
        else:
            return False

    def post_init(self):
        super().post_init()
        self.request.easyapi = {}

        # Body of Request
        self.jsonrequest = {}

        request.easyapi = dict(
            record=self.api_record,
            error_debug=self.api_record.error_debug,
            error_detail=self.api_record.error_detail,
            pagesize=self.api_record.page_size
        )

    def url_match(self):
        """Identify parameters from URL.

        /res.partner
        /res.partner/1
        /res.partner/1/parent_id
        /res.partner/1/relationships/parent_id
        ToDo: /res.partner/1/relationships/parent_id/5
        """
        endpoint = request.base_endpoint
        urls = Map([
            Rule(f'/{endpoint}/<string:{RESOURCE}>'),
            Rule(f'/{endpoint}/<string:{RESOURCE}>/<int:{RESOURCE_ID}>'),
            Rule(f'/{endpoint}/<string:{RESOURCE}>/<int:{RESOURCE_ID}>/<string:{RELATION}>/<string:{RESOURCE_ATTR}>'),
            Rule(f'/{endpoint}/<string:{RESOURCE}>/<int:{RESOURCE_ID}>/<string:{RESOURCE_ATTR}>'),
            Rule('/<path:url>')
        ]).bind('')
        return urls.match(self.request.httprequest.path)[1]


    def pre_process(self):
        """Prepare the process so it can be easy served by subsequent api."""
        super().pre_process()
        self.request.easyapi.update(self.url_match())

    def process_request(self, endpoint, args):
        """JsonAPI Process Invoke Entry"""

        self.request.params = self.request.get_http_params()
        if request.httprequest.get_data(as_text=True):
            values = json.loads(request.httprequest.get_data(as_text=True))
            ctx = values.get('context')
            if ctx is None and 'context' in values.get('data', {}):
                ctx = values.get('data', {}).get('context')
            if ctx is not None and self.request.db:
                self.request.update_context(**ctx)

        try:
            if self.request.db:
                result = self.request.registry['ir.http']._dispatch(endpoint)
            else:
                # ToDo: Raise DB Error.
                result = endpoint(**self.request.params)
        except AccessError as exc:
            raise AuthorizationFailureException(exc.args)
        except ValidationError as exc:
            raise JsonApiValidationError(exc.args)
        except JsonAPIException as exc:
            raise exc
        except Exception as exc:
            raise BadRequestException(exc.args)
        else:
            return self.make_api_response(result)

    def handle_error(self, exc):
        extra_headers = []
        if isinstance(exc,JsonAPIException):
            error = exc.to_json_api_error()
            status = exc.status_code
        elif isinstance(exc, AccessDenied):
            jsonapi_exception = AuthenticationFailureException(exc.args)
            error = jsonapi_exception.to_json_api_error()
            status = jsonapi_exception.status_code
        elif isinstance(exc, Unauthorized):
            jsonapi_exception = AuthenticationFailureException(exc.description)
            error = jsonapi_exception.to_json_api_error()
            status = jsonapi_exception.status_code
            extra_headers = exc.get_headers()
        else:
            jsonapi_exception = BadRequestException(exc.args)
            error = jsonapi_exception.to_json_api_error()
            status = 400
        error.update({'debug': traceback.format_exc()}) if request.easyapi.get('error_debug') else None
        error.pop('detail') if not request.easyapi.get('error_detail') else None
        data = json.dumps(error, ensure_ascii=False, default=json_default)
        headers = Headers([('Content-Type', 'application/vnd.api+json')])
        headers['Content-Length'] = len(data)
        headers.extend(extra_headers)
        return Response(data, headers=headers, status=status)

    def make_api_response(self, result):
        if isinstance(result, Response) and hasattr(result, 'is_api') and result.is_api:
            result.flatten()
        elif not isinstance(result, Response):
            result = self.make_basic_json_response(result)
        return result

    def make_basic_json_response(self, result):
        data = json.dumps(result, ensure_ascii=False, default=json_default)
        headers = Headers([('Content-Type', 'application/vnd.api+json')])
        headers['Content-Length'] = len(data)
        return Response(data, headers=headers, status=200)
