# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from base64 import b64encode

from odoo import models
from odoo.http import request


class AuthSignUpJsonAPI(models.AbstractModel):
    _inherit = 'easy.jsonapi.public.methods'

    @classmethod
    def allowed_public(cls):
        res = super().allowed_public()
        res.extend(['register', 'login', 'changepassword', 'info'])
        return res

    @classmethod
    def register(cls, query, response):
        data = request.get_json_data()

        # Signup Must Require login, name and password as data in body.
        if not all([x in data and data[x] for x in ['login', 'name', 'password']]):
            raise Exception("Invalid Use of Method.")

        login, passwd = request.env['res.users'].sudo().signup({
            'login': data['login'],
            'name': data['name'],
            'password': data['password'],
        })
        request.env.cr.commit()     # as authenticate will use its own cursor we need to commit the current transaction
        credential = {'login': data.get('login'), 'password': data.get('password'), 'type': 'password'}
        auth_info = request.session.authenticate(request.db, credential)
        pre_uid = auth_info.get('uid')
        if not pre_uid:
            raise Exception('Authentication Failed.')

        # Combine username and password with a colon
        credentials = f'{login}:{passwd}'
        # Encode the credentials using Base64
        token = b64encode(credentials.encode('utf-8')).decode('utf-8')
        response.jsonapi_data = {
            'result': 'Signup Successful',
            'token': f'basic {token}',
            'user_id': pre_uid
        }
        return response

    @classmethod
    def login(cls, query, response):
        data = request.get_json_data()
        # Signup Must Require login, name and password as data in body.
        if not all([x in data and data[x] for x in ['login', 'password']]):
            raise Exception("Invalid Use of Method.")
        login = data['login']
        passwd = data['password']
        credential = {'login': login, 'password': passwd, 'type': 'password'}
        auth_info = request.session.authenticate(request.db, credential)
        pre_uid = auth_info.get('uid')
        if not pre_uid:
            raise Exception('Authentication Failed.')
        # Combine username and password with a colon
        credentials = f'{login}:{passwd}'
        # Encode the credentials using Base64
        token = b64encode(credentials.encode('utf-8')).decode('utf-8')
        response.jsonapi_data = {
            'result': 'Login Successful',
            'token': f'basic {token}',
            'user_id': pre_uid
        }
        return response

    @classmethod
    def changepassword(cls, query, response):
        data = request.get_json_data()
        # Signup Must Require login, name and password as data in body.
        if not all([x in data and data[x] for x in ['login', 'password', 'new_password']]):
            raise Exception("Invalid Use of Method.")
        login = data['login']
        passwd = data['password']
        new_passwd = data['new_password']
        credential = {'login': login, 'password': passwd, 'type': 'password'}
        auth_info = request.session.authenticate(request.db, credential)
        pre_uid = auth_info.get('uid')
        if not pre_uid:
            raise Exception('Authentication Failed.')
        the_user = request.env['res.users'].browse(pre_uid)
        the_user.change_password(passwd, new_passwd)
        request.env.cr.commit()
        credential = {'login': login, 'password': new_passwd, 'type': 'password'}
        auth_info = request.session.authenticate(request.db, credential)
        pre_uid = auth_info.get('uid')
        if not pre_uid:
            raise Exception('Unable to change password of the user.')
        # Combine username and password with a colon
        credentials = f'{login}:{new_passwd}'
        # Encode the credentials using Base64
        token = b64encode(credentials.encode('utf-8')).decode('utf-8')
        response.jsonapi_data = {
            'result': 'Password Update Successful',
            'token': f'basic {token}',
            'user_id': pre_uid
        }
        return response

    @classmethod
    def info(cls, query, response):
        response.jsonapi_data = {
            'result': 'Json:API Call Successful.',
        }
        return response
