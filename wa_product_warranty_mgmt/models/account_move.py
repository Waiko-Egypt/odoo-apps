# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class AccountMove(models.Model):
    _inherit = "account.move"

    def _post(self, soft=True):
        """Override _post to calculate warranty dates on invoice confirmation."""
        posted = super()._post(soft=soft)
        for move in posted:
            if move.move_type in ("out_invoice", "out_refund"):
                confirmation_date = move.invoice_date or fields.Date.context_today(move)
                for line in move.invoice_line_ids.filtered(
                    lambda l: l.product_id and l.warranty_duration > 0
                ):
                    line.warranty_start_date = confirmation_date
                    if line.warranty_period_type == "years":
                        line.warranty_end_date = confirmation_date + relativedelta(
                            years=line.warranty_duration
                        )
                    else:
                        line.warranty_end_date = confirmation_date + relativedelta(
                            months=line.warranty_duration
                        )
        return posted
