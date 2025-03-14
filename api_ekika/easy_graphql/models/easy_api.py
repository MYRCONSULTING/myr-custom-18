# -*- coding: utf-8 -*-
######################################################################
#                                                                    #
# Part of EKIKA CORPORATION PRIVATE LIMITED (Website: ekika.co).     #
# See LICENSE file for full copyright and licensing details.         #
#                                                                    #
######################################################################

from odoo import models, fields, api

class EasyApi(models.Model):
    _inherit = 'easy.api'

    api_type = fields.Selection(selection_add=[('graphql','GraphQL')], default='graphql')
    easy_graphql_doc_id = fields.Many2one('easy.graphql.doc', 'GraphQl Doc')

    def action_graphql_doc(self):
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id(
            'easy_graphql.action_easy_graphql_doc')
        action['res_id'] = self.easy_graphql_doc_id.id
        action['view_mode'] = 'form'
        action['views'] = [[self.env.ref('easy_graphql.view_easy_graphql_doc_form').id, 'form']]
        return action

    @api.model_create_multi
    def create(self, vals_list):
        results = super().create(vals_list)
        for result in results:
            if result.api_type == 'graphql':
                doc = self.env['easy.graphql.doc'].create({
                    'name': f'{result.name}_DOC',
                    'easy_api_id': result.id
                    })
                result.easy_graphql_doc_id = doc.id

                # routing table can be reload using clear_cache() method, no need to restart server
                # self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
                #     'type': 'warning',
                #     'title': "Your API endpoint is created.",
                #     'message': 'Warning: A server restart is required for the GraphQL endpoint changes to take effect.',
                #     'sticky': True
                # })
        return results

    def write(self, vals):
        api_type = vals.get('api_type')
        if api_type:
            if api_type == 'graphql':
                if not self.easy_graphql_doc_id:
                    doc = self.env['easy.graphql.doc'].create({
                        'name': f'{self.name}_DOC',
                        'easy_api_id': self.id
                        })
                    self.easy_graphql_doc_id = doc.id
            else:
                if self.easy_graphql_doc_id:
                    self.easy_graphql_doc_id.unlink()
        res = super().write(vals)

        # routing table can be reload using clear_cache() method, no need to restart server
        # if res and vals.get('base_endpoint'):
        #     self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
        #         'type': 'warning',
        #         'title': "Your API endpoint is updated.",
        #         'message': 'Warning: A server restart is required for the GraphQL endpoint changes to take effect.',
        #         'sticky': True
        #     })
        #     return res
        return res

    def unlink(self):
        for record in self:
            if record.easy_graphql_doc_id:
                record.easy_graphql_doc_id.unlink()
        return super().unlink()

    @api.depends('api_type')
    def _compute_api_type_help(self):
        super()._compute_api_type_help()
        for rec in self:
            if rec.api_type == 'graphql':
                help_msg = ('<b>Api Type</b>: This field describe which type of api you are '
                            'going to use, currently it is GraphQL, For more Details Go to: '
                            '<a href="https://graphql.org/learn/" target="_blank" class=""'
                            'data-bs-original-title="" title="">Introduction to GraphQL</a>')
                rec.api_type_help = help_msg

