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
    def _auth_method_api(cls):
        super()._auth_method_api()
        if request.resource_control_type == 'custom_access':
            getattr(cls, f'_auth_method_{request.auth_type}')()
            if request.dispatcher.api_record.resource_control_id:
                invokeuser = request.dispatcher.api_record.resource_control_id.user_id.id
            else:
                invokeuser = None
            request.update_env(user=invokeuser)
        elif request.resource_control_type == False:
            raise Exception()
