# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo.http import request
from odoo.addons.api_framework_base.api_dispatcher import BaseAPIDispatcher

ALL_ORIGINS = '*'

class BaseAPIDispatcherCors(BaseAPIDispatcher):

    def remove_cors_headers(self):
        request.future_response.headers.remove('Access-Control-Allow-Origin')
        request.future_response.headers.remove('Access-Control-Allow-Methods')

    def manage_cors_headers(self):
        if request.future_response.headers.get('Access-Control-Allow-Origin') == 'api':
            if hasattr(request.easyapi['record'], 'allowed_origins') and request.easyapi['record'].allowed_origins:
                allowed_origins = [x.strip().strip('/') for x in request.easyapi['record'].allowed_origins.split(',')]
                if ALL_ORIGINS in allowed_origins:
                    request.future_response.headers.set('Access-Control-Allow-Origin', ALL_ORIGINS)
                elif request.httprequest.headers.get('origin') in allowed_origins:
                    request.future_response.headers.set('Access-Control-Allow-Origin', 
                                                        request.httprequest.headers.get('origin'))
                else:
                    self.remove_cors_headers()
            else:
                self.remove_cors_headers()
        else:
            self.remove_cors_headers()
