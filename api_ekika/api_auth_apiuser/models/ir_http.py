# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo import models
from odoo.http import request
from odoo.exceptions import AccessDenied

ACCESS_TOKEN_LENGTH = 64


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def verify_user(cls, username, password, su=None):
        credential = {
            'login': username,
            'password': password,
            'type': 'password'
        }
        user_info = request.env['res.users']._login(
            request.db, credential, request.env)
        if user_info and 'uid' in user_info and user_info['uid']:
            request.update_env(user=user_info['uid'], su=su)

    @classmethod
    def _auth_method_apiuser(cls, su=None):
        username = request.httprequest.headers.get('username')
        password = request.httprequest.headers.get('password')
        if username and password:
            cls.verify_user(username, password, su)
        else:
            raise AccessDenied('Please Pass Credentials as per document in Header')
