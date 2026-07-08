# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class PosOrder(models.Model):
    _inherit = "pos.order"

    def _process_order(self, order, draft, existing_order):
        """Override to compute warranty dates on POS order confirmation."""
        order_id = super()._process_order(order, draft, existing_order)
        pos_order = self.browse(order_id)
        if pos_order and pos_order.state in ("paid", "done", "invoiced"):
            confirmation_date = (
                pos_order.date_order.date()
                if pos_order.date_order
                else fields.Date.context_today(pos_order)
            )
            for line in pos_order.lines:
                product = line.product_id
                if product and product.product_tmpl_id.warranty_duration > 0:
                    tmpl = product.product_tmpl_id
                    start_date = confirmation_date
                    if tmpl.warranty_period_type == "years":
                        end_date = start_date + relativedelta(
                            years=tmpl.warranty_duration
                        )
                    else:
                        end_date = start_date + relativedelta(
                            months=tmpl.warranty_duration
                        )
                    # If POS order has an associated invoice, update invoice lines
                    if pos_order.account_move:
                        for (
                            inv_line
                        ) in pos_order.account_move.invoice_line_ids.filtered(
                            lambda l: l.product_id == product
                        ):
                            inv_line.warranty_start_date = start_date
                            inv_line.warranty_end_date = end_date
        return order_id
