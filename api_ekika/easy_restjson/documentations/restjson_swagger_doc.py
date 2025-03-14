# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo import models
from odoo.http import request


class RestJsonSwaggerDoc(models.AbstractModel):
    _name = 'restjson.swagger.doc'
    _description = 'Restjson Swagger Doc'

    @classmethod
    def swagger_doc(cls, api_endpoint):
        doc = cls._swagger_doc(api_endpoint)
        return doc

    @classmethod
    def _swagger_doc(cls, api_endpoint):
       return {
            'swagger': cls._swagger_version(api_endpoint),
            'info': cls._swagger_info(api_endpoint),
            'host': cls._swagger_host(api_endpoint),
            'basePath': cls._swagger_base_path(api_endpoint),
            'tags': cls._swagger_tags(api_endpoint),
            'schemes': cls._swagger_schemes(api_endpoint),
            'paths': cls._register_paths(api_endpoint)
        }

    @classmethod
    def _swagger_version(cls, api_endpoint):
        return '2.0'

    @classmethod
    def _swagger_info(cls, api_endpoint) -> dict:
        return {
            "title": api_endpoint.name,
            "description": api_endpoint.description,
            "version": "1.0.0",
        }

    @classmethod
    def _swagger_host(cls, api_endpoint):
        return request.env['ir.config_parameter'].sudo().get_param(
            'web.base.url', default=''
        ).replace('http://', '').replace('https://', '')

    @classmethod
    def _swagger_base_path(cls, api_endpoint):
        return f'/{api_endpoint.base_endpoint}'

    @classmethod
    def _swagger_tags(cls, api_endpoint):
        return [
            {
                "name": "Dynamic",
                "description": "Dynamic Model Method calls",
            }
        ]

    @classmethod
    def _swagger_schemes(cls, api_endpoint):
        base_url = request.env['ir.config_parameter'].sudo().get_param(
            'web.base.url', default=''
        )
        return ['https'] if base_url.startswith('https') else ['http']

    @classmethod
    def _register_paths(cls, api_endpoint):
        return {
            "/{model}/create": cls._create_path(api_endpoint),
            "/{model}/read": cls._read_path(api_endpoint),
            "/{model}/write": cls._write_path(api_endpoint),
            "/{model}/unlink": cls._unlink_path(api_endpoint),
            "/{model}/search_read": cls._search_read_path(api_endpoint),
            "/{model}/search": cls._search_path(api_endpoint),
            "/{model}/search_count": cls._search_count_path(api_endpoint),
            "/{model}/read_group": cls._read_group_path(api_endpoint),
            "/{model}/fields_get": cls._fields_get_path(api_endpoint),
            "/{model}/check_access_rights": cls._check_access_rights_path(api_endpoint),
            "/{model}/{method}": cls._method_path(api_endpoint),
        }

    @classmethod
    def _search_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Retrieve Record ID",
                "description": "Perform this action to search and retrieve the unique ID of a specific record.",
                "parameters": cls._search_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                        "type": "array",
                        "items": {
                            "type": "integer"
                        },
                        "example": [1, 2, 3, 4]
                        }
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _search_read_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Fetch Record Details",
                "description": " Perform a search to read the details of specific records, including all specified fields",
                "parameters": cls._search_read_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._search_read_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _search_count_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Retrieve Total Record Count",
                "description": "This operation searches and returns the total count of records matching the specified criteria.",
                "parameters": cls._search_count_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "type": "integer",
                            "example": 6
                        }
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _read_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Retrieve Record Details",
                "description": "Use this operation to retrieve the field values of a particular record identified by its ID.",
                "parameters": cls._read_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._read_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _read_group_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Retrieve Grouped Data",
                "description": "This operation fetches records and grouped by a particular field based on defined parameters.",
                "parameters": cls._read_group_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._read_group_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _fields_get_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Get Field Details",
                "description": "This operation is used to fetch detailed information about various fields in the system.",
                "parameters": cls._fields_get_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._fields_get_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _check_access_rights_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Verify Access Permissions",
                "description": "Use this operation to verify the different access rights associated with a model.",
                "parameters": cls._check_access_rights_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._check_access_rights_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _method_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Method Execution",
                "description": "Execute the specified method and retrieve the result or output generated by that method.",
                "parameters": cls._method_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._method_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _create_path(cls, api_endpoint):
        return {
            "post": {
                "tags": ["Dynamic"],
                "summary": "Add New Record",
                "description": "This operation allows you to create a new record in the system.",
                "parameters": cls._create_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._create_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _write_path(cls, api_endpoint):
        return {
            "patch": {
                "tags": ["Dynamic"],
                "summary": "Modify Record",
                "description": "This operation allows you to edit an existing record in the system.",
                "parameters": cls._write_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._write_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _unlink_path(cls, api_endpoint):
        return {
            "delete": {
                "tags": ["Dynamic"],
                "summary": "Remove Record",
                "description": "This operation allows you to delete a specific record from the system.",
                "parameters": cls._unlink_parameters(api_endpoint) + cls._swagger_restjson_parameters(api_endpoint),
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": cls._unlink_200_schema(api_endpoint)
                    },
                    "401": cls._default_401_response(),
                    "400": cls._default_400_response()
                }
            }
        }

    @classmethod
    def _search_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Search Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[["is_company", "=", True]]],
                    "kwargs": {}
                }
              }
            }
        ]

    @classmethod
    def _search_read_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Search Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[["is_company", "=", True]]],
                    "kwargs": {"fields": ["name", "country_id", "comment", "is_company"], "limit": 2}
                }
              }
            }
        ]

    @classmethod
    def _read_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Read Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[14, 10]],
                    "kwargs": {"fields": ["name", "country_id", "comment", "is_company"]}
                }
              }
            }
        ]

    @classmethod
    def _read_group_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Read Group Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[["is_company", "=", False]]],
                    "kwargs": {"fields": ["name", "country_id", "comment", "is_company"], "groupby": "country_id"}
                }
              }
            }
        ]

    @classmethod
    def _fields_get_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Fields Get Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [],
                    "kwargs": {"attributes": ["string", "help", "type"]}
                }
              }
            }
        ]

    @classmethod
    def _check_access_rights_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Check Access Rights Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": ["create"],
                    "kwargs": {}
                }
              }
            }
        ]

    @classmethod
    def _method_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Method Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
              }
            }
        ]

    @classmethod
    def _create_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Create Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [{"name": "Sample Partner", "email": "sample-partner@example.com"}],
                    "kwargs": {}
                }
              }
            }
        ]

    @classmethod
    def _write_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Write Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[41], {"name": "Sample Partner Change", "email": "sample-partner-change@example.com"}],
                    "kwargs": {}
                }
              }
            }
        ]

    @classmethod
    def _unlink_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Unlink Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[41]],
                    "kwargs": {}
                }
              }
            }
        ]

    @classmethod
    def _search_count_parameters(cls, api_endpoint):
        return [
            {
                "in": "body",
                "name": "body",
                "description": "Search Parameters Body",
                "required": True,
                "schema": {
                "type": "object",
                "properties": {
                  "args": {
                    "type": "array",
                    "description": "An array of arguments",
                    "example": []
                  },
                  "kwargs": {
                    "type": "object",
                    "description": "A dictionary of additional key-value pairs.",
                    "additionalProperties": True,
                    "example": {}
                  }
                },
                "example": {
                    "args": [[["is_company", "=", True]]],
                    "kwargs": {}
                }
              }
            }
        ]

    @classmethod
    def _search_read_200_schema(cls, api_endpoint):
        return {
            "type": "array",
            "items": {
            "type": "object",
            },
            "example": [
            {
                "id": 15,
                "name": "Azure Interior",
                "country_id": [233, "United States"],
                "comment": False,
                "is_company": True
            },
            {
                "id": 10,
                "name": "Deco Addict",
                "country_id": [233, "United States"],
                "comment": False,
                "is_company": True
            }
            ]
        }

    @classmethod
    def _read_200_schema(cls, api_endpoint):
        return {
            "type": "array",
            "items": {
            "type": "object",
            },
            "example": [
                {
                    "id": 14,
                    "name": "The Jackson Group",
                    "country_id": [
                    233,
                    "United States"
                    ],
                    "comment": False,
                    "is_company": True
                },
                {
                    "id": 10,
                    "name": "Deco Addict",
                    "country_id": [
                    233,
                    "United States"
                    ],
                    "comment": False,
                    "is_company": True
                },
            ]
        }

    @classmethod
    def _read_group_200_schema(cls, api_endpoint):
        return {
            "type": "array",
            "items": {
                "type": "object",
            },
            "example": [
                {
                    "country_id": [
                    233,
                    "United States"
                    ],
                    "country_id_count": 28,
                    "__domain": [
                    "&",
                    [
                        "is_company",
                        "=",
                        False
                    ],
                    [
                        "country_id",
                        "=",
                        233
                    ]
                    ]
                },
                {
                    "country_id": False,
                    "country_id_count": 16,
                    "__domain": [
                    "&",
                    [
                        "is_company",
                        "=",
                        False
                    ],
                    [
                        "country_id",
                        "=",
                        False
                    ]
                    ]
                }
            ]
        }

    @classmethod
    def _fields_get_200_schema(cls, api_endpoint):
        return {
            "type": "array",
            "items": {
                "type": "object",
            },
            "example": {
                "message_is_follower": {
                    "string": "Is Follower",
                    "type": "boolean"
                },
                "message_follower_ids": {
                    "string": "Followers",
                    "type": "one2many"
                },
                "message_partner_ids": {
                    "string": "Followers (Partners)",
                    "type": "many2many"
                },
                "message_ids": {
                    "string": "Messages",
                    "type": "one2many"
                },
                "has_message": {
                    "string": "Has Message",
                    "type": "boolean"
                },
                "message_needaction": {
                    "help": "If checked, new messages require your attention.",
                    "string": "Action Needed",
                    "type": "boolean"
                },
            }
        }

    @classmethod
    def _check_access_rights_200_schema(cls, api_endpoint):
        return {
            "type": None,
            "example": None
        }

    @classmethod
    def _method_200_schema(cls, api_endpoint):
        return {
            "type": "object",
        }

    @classmethod
    def _create_200_schema(cls, api_endpoint):
        return {
            "type": "integer",
            "example": 50
        }

    @classmethod
    def _write_200_schema(cls, api_endpoint):
        return {
            "type": "boolean",
            "example": True
        }

    @classmethod
    def _unlink_200_schema(cls, api_endpoint):
        return {
            "type": "boolean",
            "example": True
        }

    @classmethod
    def _swagger_restjson_parameters(cls, api_endpoint):
        return [
            {
                "name": "Content-Type",
                "in": "header",
                "required": True,
                "type": "string",
                "default": "application/json"
            },
            {
                "name": "model",
                "in": "path",
                "description": "Model Name",
                "required": True,
                "type": "string",
                "default": "res.partner"
            },
        ] + (cls._swagger_api_parameters(api_endpoint))

    @classmethod
    def _swagger_api_parameters(cls, api_endpoint) -> list:
        return [
            {
                "name": "x-api-key",
                "in": "header",
                "required": True,
                "type": "string"
            }
        ]

    @classmethod
    def _default_401_response(cls):
        return {
            "description": "Unauthorized",
            "schema": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "example": "Unauthorized"
                    },
                    "detail": {
                        "type": "string",
                        "example": "Access Denied"
                    },
                    "debug": {
                        "type": "string",
                    },
                },
                "required": ["title"]
            }
        }

    @classmethod
    def _default_400_response(cls):
        return {
            "description": "Bad Request",
            "schema": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "example": "Bad Request"
                    },
                    "detail": {
                        "type": "string",
                        "example": "Invalid Values"
                    },
                    "debug": {
                        "type": "string",
                    },
                },
                "required": ["title"]
            }
        }
