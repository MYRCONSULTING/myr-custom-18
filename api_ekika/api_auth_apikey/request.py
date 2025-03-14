# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo.http import Request

def _apikey_inject_future_response(self, response):
    # Call super by monkey-patching it.
    response = self._inject_future_response_orignal(response)
    if getattr(self, 'api_key_auth', False) and getattr(self, 'api_key_auth_cors', False) and \
                    self.httprequest.method == 'OPTIONS':
        allow_headers = response.headers.get('Access-Control-Allow-Headers')
        response.headers.set('Access-Control-Allow-Headers', f'{allow_headers}, x-api-key')
    return response

# Monkey-patch orignal method so can be called when required.
Request._inject_future_response_orignal = Request._inject_future_response
Request._inject_future_response = _apikey_inject_future_response

