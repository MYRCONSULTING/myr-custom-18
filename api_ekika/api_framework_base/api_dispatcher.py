# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from werkzeug.exceptions import NotFound
from odoo.http import Dispatcher, request
from .exceptions import UnsupportedMediaType

from abc import ABC, abstractmethod


# The request mimetypes that transport JSON in their body.
SUPPORTED_API_MIMETYPES = ('application/json', 'application/vnd.api+json', 'application/json-rpc')
JSONAPI_MIMETYPE = ('application/vnd.api+json')

CORS_MAX_AGE = 60 * 60 * 24


class EasyAPI(ABC):
    api_type: str

    # main api types. i.e. jsonapi, graphql etc.
    _apis = {}

    # Holds the record relevent to the API call.
    api_record = None

    @classmethod
    def __init_subclass__(cls):
        super().__init_subclass__()
        EasyAPI._apis[cls.api_type] = cls

    def __init__(self, request, api_record):
        self.request = request
        self.api_record = api_record

    def post_init(self):
        """Setup after init of request dispatch procedure."""
        request.base_endpoint = self.api_record.base_endpoint
        request.auth_type = self.api_record.authentication_type
        request.resource_control_type = self.api_record.resource_control_type

    @classmethod
    @abstractmethod
    def confirm_mimetype(cls, mimetype):
        """Determine if the current request is compatible with this api."""

    def pre_process(self):
        """Prepare the process so it can be easy served by subsequent api."""
        pass

    @abstractmethod
    def process_request(self, endpoint, args):
        """
        Extract the params from the request's body and call the endpoint.
        This method needs to be overridden by API implementor to process
        relevent endpoints to them.
        """

    def post_process(self, response):
        """Prepare the process so it can be easy served by subsequent api."""
        pass


class SessionExpiredException(Exception):
    pass


class BaseAPIDispatcher(Dispatcher):
    """Special Dispatcher that allows multiple type of Dispatching services
    based on configuration from api framework by ekika."""
    routing_type = 'api'

    # Identify api from database and setup to serve.
    api = None
    api_record = None

    def __init__(self, request):
        # Super's init will setup self.request
        super().__init__(request)
        if not request.env.cr.closed:
            self.post_environment_init()

    def guessBaseEndpoint(self):
        path = request.httprequest.path
        pathParts = path.split('/')
        if path.startswith('/') and len(pathParts) >= 2:
            matchBaseEndpoint = pathParts[1]
        elif len(pathParts) >= 1:
            matchBaseEndpoint = pathParts[0]
        else:
            matchBaseEndpoint = path
        return matchBaseEndpoint

    def get_api_record(self):
        if self.api_record:
            return self.api_record
        else:
            api_records = request.env['easy.api'].sudo().search(
                [('base_endpoint', '=', self.guessBaseEndpoint()),('state', '=', 'active')])
            if not api_records:
                raise NotFound
            if api_records and len(api_records) != 1:
                raise Exception('Too many API found.')
            self.api_record = api_records[0]
            return self.api_record

    def post_environment_init(self):
        """Setup API contextual environment as soon as we have connection available.
        Do not make this safe by exception cover because this is important to work well
        for our api solution. So instead let we allow to raise error if something is not
        as expected. Findout why in comments below inside def pre_dispatch.
        """
        api_record = self.get_api_record()
        api_cls = EasyAPI._apis[api_record.api_type]
        # ToDo: Allow config of CORS in API.
        if not api_cls.confirm_mimetype():
            raise UnsupportedMediaType
        self.api = api_cls(self.request, api_record)
        self.api.post_init()

    @classmethod
    def is_compatible_with(cls, request):
        if request.httprequest.accept_mimetypes.best in SUPPORTED_API_MIMETYPES:  # checks Accept
            return True
        elif request.httprequest.mimetype in SUPPORTED_API_MIMETYPES: # checks Content-Type
            return True
        else:
            raise UnsupportedMediaType

    def manage_cors_headers(self):
        """
        This method is going to be used for add/remove headers related to CORS. 
        """
        if request.future_response.headers.get('Access-Control-Allow-Origin') == 'api':
            request.future_response.headers.remove('Access-Control-Allow-Origin')
            request.future_response.headers.remove('Access-Control-Allow-Methods')

    def pre_dispatch(self, rule, args):
        """Prepare the system before dispatching the request to its controller."""

        # API Context Initialization:
        # During dispatcher initialise environment is not ready to fetch ORM records.
        # So we have to wait for api record to be available. We require before auth so we are already 
        # calling environment init from auth "def _auth_method_api".
        # But some api calls may not call auth or use some other auth method in that case we require
        # to check if api is available or not. And if it is not we initialize it.
        if self.api is None:
            self.post_environment_init()

        try:
            super().pre_dispatch(rule, args)
        except Exception as exc:
            self.manage_cors_headers()
            raise exc
        else:
            self.manage_cors_headers()
            routing = rule.endpoint.routing
            self.request.session.can_save = routing.get('save_session', False)
            self.api.pre_process()

    def dispatch(self, endpoint, args):
        """Process Request with Help of API handler."""
        return self.api.process_request(endpoint, args)

    def handle_error(self, exc):
        return self.api.handle_error(exc)

