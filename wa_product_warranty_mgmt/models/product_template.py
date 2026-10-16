# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    warranty_duration = fields.Integer(
        string="Warranty Duration",
        default=0,
        help="Number of months or years for the warranty period.",
    )
    warranty_period_type = fields.Selection(
        selection=[
            ("months", "Months"),
            ("years", "Years"),
        ],
        string="Warranty Period Type",
        default="months",
        help="Select whether the warranty duration is in months or years.",
    )
    warranty_description = fields.Char(
        string="Warranty",
        compute="_compute_warranty_description",
        store=True,
        help="Auto-generated warranty description for reports.",
    )

    @api.depends("warranty_duration", "warranty_period_type")
    def _compute_warranty_description(self):
        for product in self:
            if product.warranty_duration and product.warranty_period_type:
                period_label = dict(
                    product._fields["warranty_period_type"].selection
                ).get(product.warranty_period_type, "")
                product.warranty_description = "%d %s" % (
                    product.warranty_duration,
                    period_label,
                )
            else:
                product.warranty_description = ""
