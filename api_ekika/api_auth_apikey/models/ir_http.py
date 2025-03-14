# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from datetime import datetime
from odoo import models
from odoo.http import request
from odoo.exceptions import AccessDenied

ACCESS_TOKEN_LENGTH = 64


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def verify_api_key(cls, apikey, su=None):
        api_key = request.easyapi['record'].api_key_ids.filtered_domain(
            [('apikey', '=', apikey)])
        if len(api_key) != 1:
            raise AccessDenied('Access Denied')
        current_time = datetime.now().replace(microsecond=0)

        if current_time > api_key.expiry:
            raise AccessDenied('Access Denied')
        user = api_key.user_id
        request.update_env(user=user, su=su)

    @classmethod
    def _auth_method_apikey(cls, su=None):
        if request.httprequest.headers.get('x-api-key'):
            apikey = request.httprequest.headers.get('x-api-key')
            cls.verify_api_key(apikey, su=su)
        else:
            raise AccessDenied('Access Denied')

    @classmethod
    def _pre_dispatch(cls, rule, args):
        if request.httprequest.method == 'OPTIONS' and rule.endpoint.routing.get('cors', False):
            request._set_request_dispatcher(rule)
        if (rule.endpoint.routing['auth'] == 'api' or hasattr(request, 'easyapi')) and \
                    request.easyapi['record'].authentication_type == 'apikey':
            request.api_key_auth = True
            if rule.endpoint.routing.get('cors'):
                request.api_key_auth_cors = True
        elif rule.endpoint.routing['auth'] == 'apikey':
            request.api_key_auth = True
            if rule.endpoint.routing.get('cors'):
                request.api_key_auth_cors = True
        super()._pre_dispatch(rule, args)

