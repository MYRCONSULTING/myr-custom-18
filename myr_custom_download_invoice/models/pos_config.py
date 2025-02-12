from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    auto_download_invoice_after_validate_order = fields.Boolean(string='Download invoice automatically after validate order with invoice option enable', default=True,
                    help="Choose this if you want to the system automatically download the invoice after validate order for customer who take invoice")
