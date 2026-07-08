# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    warranty_duration = fields.Integer(
        string="Warranty Duration",
        related="product_id.product_tmpl_id.warranty_duration",
        store=True,
        readonly=True,
    )
    warranty_period_type = fields.Selection(
        string="Warranty Period Type",
        related="product_id.product_tmpl_id.warranty_period_type",
        store=True,
        readonly=True,
    )
    warranty_description = fields.Char(
        string="Warranty",
        related="product_id.product_tmpl_id.warranty_description",
        store=True,
        readonly=True,
    )
