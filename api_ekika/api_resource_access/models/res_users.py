# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo.osv import expression
from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_personalized_access = fields.Boolean()

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=100, order=None):
        domain = domain or []
        user_ids = []
        if operator not in expression.NEGATIVE_TERM_OPERATORS:
            if operator == 'ilike' and not (name or '').strip():
                name_domain = [('is_personalized_access','=',False)]
            else:
                name_domain = [('login', '=', name),('is_personalized_access','=',False)]
            user_ids = self._search(expression.AND([name_domain, domain]), limit=limit,
                                    order=order)
        if not user_ids:
            new_domain = [('is_personalized_access','=',False)]
            user_ids = self._search(expression.AND([[('name', operator, name)], domain, new_domain]),
                                    limit=limit, order=order)
        return user_ids
