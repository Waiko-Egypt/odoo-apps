from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    show_product_image_in_reports = fields.Boolean(
        string="Show Product Image in Reports",
        default=True,
        help="Display product image in sale order and invoice report lines.",
    )
    product_image_width = fields.Integer(
        string="Product Image Width (px)",
        default=40,
        help="Width of the product image in pixels in report lines.",
    )
    product_image_height = fields.Integer(
        string="Product Image Height (px)",
        default=40,
        help="Height of the product image in pixels in report lines.",
    )
