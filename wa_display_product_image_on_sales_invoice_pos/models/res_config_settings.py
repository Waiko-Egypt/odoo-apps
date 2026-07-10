from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_product_image_in_reports = fields.Boolean(
        related="company_id.show_product_image_in_reports",
        readonly=False,
        string="Show Product Image in Reports",
        help="Display product image in sale order and invoice report lines.",
    )
    product_image_width = fields.Integer(
        related="company_id.product_image_width",
        readonly=False,
        string="Product Image Width (px)",
        help="Width of the product image in pixels in report lines.",
    )
    product_image_height = fields.Integer(
        related="company_id.product_image_height",
        readonly=False,
        string="Product Image Height (px)",
        help="Height of the product image in pixels in report lines.",
    )
