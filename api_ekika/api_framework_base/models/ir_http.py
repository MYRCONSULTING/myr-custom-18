# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from werkzeug.routing import UnicodeConverter

from odoo import models
from odoo.http import request


class ApiConverter(UnicodeConverter):
    pass


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _get_converters(cls):
        """Attach API Converter to match dynamic route."""
        return dict(
            super()._get_converters(),
            api=ApiConverter,
        )

    @classmethod
    def _auth_method_api(cls):
        request.dispatcher.post_environment_init()
        if hasattr(request, 'auth_type'):
            if request.resource_control_type == 'user_based':
                getattr(cls, f'_auth_method_{request.auth_type}')()
            elif request.resource_control_type == 'full_access':
                getattr(cls, f'_auth_method_{request.auth_type}')(su=True)
            elif request.resource_control_type == False:
                raise Exception()
        else:
            raise Exception()

