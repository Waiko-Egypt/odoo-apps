from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    product_image = fields.Binary(
        related="product_id.image_128",
        string="Product Image",
        store=False,
    )
