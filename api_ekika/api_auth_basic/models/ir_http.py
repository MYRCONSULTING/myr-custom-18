# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

import base64
from odoo import models
from odoo.http import request
from odoo.modules.registry import Registry
from ..exceptions import BasicUnauthorized


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _auth_method_basic(cls, su=None):
        if request.httprequest.headers.get('Authorization'):
            authorization_header = request.httprequest.headers.get('Authorization')
            if authorization_header.split()[0].lower() != 'basic':
                raise BasicUnauthorized('The basic authentication header is not valid.')
            try:
                base64_bytes = authorization_header.split()[1].encode("ascii")
                credentials_bytes = base64.b64decode(base64_bytes)
                credentials = credentials_bytes.decode("ascii").split(':')
                username = credentials[0]
                password = credentials[1]
            except Exception as exc:
                msg = ('The basic authentication header is not valid. '
                'The credentials are not properly encoded using base64.')
                raise BasicUnauthorized(msg) from exc
            try:
                registry = Registry(request.db)
                credential = {
                    'login': username,
                    'password': password,
                    'type': 'password'
                }
                user_info = registry['res.users']._login(request.db, credential, request.env)
                if user_info and 'uid' in user_info and user_info['uid']:
                    request.update_env(user=user_info['uid'], su=su)

            except Exception as exc:
                raise BasicUnauthorized('Incorrect Credentials') from exc
        else:
            raise BasicUnauthorized('Authorization Header Not Provided!')
