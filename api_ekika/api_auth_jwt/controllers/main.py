# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

import jwt
from datetime import datetime, timedelta
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessDenied
from ..utils import SYMMETRIC_ALGORITHMS, ASYMMETRIC_ALGORITHMS


class JWTAuthController(http.Controller):
    @http.route('/_api_jwt_user_login', type='api', auth='public', methods=['POST'], cors='api', csrf=False)
    def jwt_login(self, **kwargs):
        """ Authenticate user and return a JWT token """
        data = request.get_json_data()
        try:
            credential = {'login': data.get('login'), 'password': data.get('password'), 'type': 'password'}
            auth_info = request.session.authenticate(request.db, credential)
            user = request.env['res.users'].browse(auth_info['uid'])
            token = self.create_api_jwt_token(user)
            return {
                'token': token,
            }
        except Exception as exc :
            raise AccessDenied('Access Denied')

    def create_api_jwt_token(self, user):
        expiry_hours = self.get_expiry_hour_time()
        # Create payload
        payload = {
            "sub": user.id,  # Subject: User identifier
            "name": user.name,
            "exp": datetime.now() + timedelta(hours=float(expiry_hours))  # Token expiration time
        }
        jwt_algorithm = self.get_jwt_algorithm()
        if jwt_algorithm in SYMMETRIC_ALGORITHMS:
            token = self.generate_symmetric_key_jwt_token(payload, jwt_algorithm)
        elif jwt_algorithm in ASYMMETRIC_ALGORITHMS:
            token = self.generate_asymmetric_key_jwt_token(payload, jwt_algorithm)
        return token

    def generate_symmetric_key_jwt_token(self, payload, jwt_algo):
        jwt_secret_key = self.get_jwt_secret_key()
        token = jwt.encode(payload, jwt_secret_key, jwt_algo)
        return token

    def generate_asymmetric_key_jwt_token(self, payload, jwt_algo):
        jwt_private_key = self.get_jwt_private_key()
        token = jwt.encode(payload, jwt_private_key, jwt_algo)
        return token

    def get_expiry_hour_time(self):
        return request.easyapi['record'].jwt_expiry_time_hours

    def get_jwt_algorithm(self):
        return request.easyapi['record'].api_jwt_algo

    def get_jwt_secret_key(self):
        return request.easyapi['record'].jwt_secret_key

    def get_jwt_private_key(self):
        return request.easyapi['record'].jwt_private_key
