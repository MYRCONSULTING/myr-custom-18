from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_auto_download_invoice_after_validate_order = fields.Boolean(related='pos_config_id.auto_download_invoice_after_validate_order', readonly=False)
