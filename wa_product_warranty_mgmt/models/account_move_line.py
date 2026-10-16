# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

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
    warranty_start_date = fields.Date(
        string="Warranty Start Date",
        help="Start date of the warranty, set when invoice is confirmed.",
    )
    warranty_end_date = fields.Date(
        string="Warranty End Date",
        help="End date of the warranty, calculated from start date + duration.",
    )
