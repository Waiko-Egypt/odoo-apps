from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StampSignatureWizard(models.TransientModel):
    _name = "stamp.signature.wizard"
    _description = "Upload Company Stamp & Signature"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )

    # ── Stamp ─────────────────────────────────────────────────────────────────
    company_stamp = fields.Binary(
        string="Stamp Image",
        related="company_id.company_stamp",
        readonly=False,
    )
    company_stamp_filename = fields.Char(
        related="company_id.company_stamp_filename",
        readonly=False,
    )
    stamp_width = fields.Integer(
        related="company_id.stamp_width",
        readonly=False,
        string="Width (px)",
    )
    stamp_height = fields.Integer(
        related="company_id.stamp_height",
        readonly=False,
        string="Height (px)",
    )
    stamp_opacity = fields.Float(
        related="company_id.stamp_opacity",
        readonly=False,
        string="Opacity",
        digits=(3, 2),
    )
    stamp_position = fields.Selection(
        related="company_id.stamp_position",
        readonly=False,
        string="Position",
    )
    stamp_rotation = fields.Integer(
        related="company_id.stamp_rotation",
        readonly=False,
        string="Rotation (°)",
    )
    stamp_as_watermark = fields.Boolean(
        related="company_id.stamp_as_watermark",
        readonly=False,
        string="Use as Watermark",
    )
    stamp_expiry_date = fields.Date(
        related="company_id.stamp_expiry_date",
        readonly=False,
        string="Expiry Date",
    )
    stamp_is_expired = fields.Boolean(
        related="company_id.stamp_is_expired",
        string="Is Expired",
    )
    print_stamp_on_quotation = fields.Boolean(
        related="company_id.print_stamp_on_quotation",
        readonly=False,
        string="Quotations / Sale Orders",
    )
    print_stamp_on_invoice = fields.Boolean(
        related="company_id.print_stamp_on_invoice",
        readonly=False,
        string="Invoices",
    )
    print_stamp_on_delivery = fields.Boolean(
        related="company_id.print_stamp_on_delivery",
        readonly=False,
        string="Delivery Notes",
    )
    print_stamp_on_purchase = fields.Boolean(
        related="company_id.print_stamp_on_purchase",
        readonly=False,
        string="Purchase Orders",
    )

    # ── Signature ──────────────────────────────────────────────────────────────
    company_signature = fields.Binary(
        string="Signature Image",
        related="company_id.company_signature",
        readonly=False,
    )
    company_signature_filename = fields.Char(
        related="company_id.company_signature_filename",
        readonly=False,
    )
    signature_width = fields.Integer(
        related="company_id.signature_width",
        readonly=False,
        string="Width (px)",
    )
    signature_height = fields.Integer(
        related="company_id.signature_height",
        readonly=False,
        string="Height (px)",
    )
    signature_opacity = fields.Float(
        related="company_id.signature_opacity",
        readonly=False,
        string="Opacity",
        digits=(3, 2),
    )
    signature_position = fields.Selection(
        related="company_id.signature_position",
        readonly=False,
        string="Position",
    )
    signature_rotation = fields.Integer(
        related="company_id.signature_rotation",
        readonly=False,
        string="Rotation (°)",
    )
    signature_expiry_date = fields.Date(
        related="company_id.signature_expiry_date",
        readonly=False,
        string="Expiry Date",
    )
    signature_is_expired = fields.Boolean(
        related="company_id.signature_is_expired",
        string="Signature Is Expired",
    )
    show_signatory_label = fields.Boolean(
        related="company_id.show_signatory_label",
        readonly=False,
        string="Show Signatory Label",
    )
    authorized_signatory_label = fields.Char(
        related="company_id.authorized_signatory_label",
        readonly=False,
        string="Label Text",
    )
    print_signature_on_quotation = fields.Boolean(
        related="company_id.print_signature_on_quotation",
        readonly=False,
        string="Quotations / Sale Orders",
    )
    print_signature_on_invoice = fields.Boolean(
        related="company_id.print_signature_on_invoice",
        readonly=False,
        string="Invoices",
    )
    print_signature_on_delivery = fields.Boolean(
        related="company_id.print_signature_on_delivery",
        readonly=False,
        string="Delivery Notes",
    )
    print_signature_on_purchase = fields.Boolean(
        related="company_id.print_signature_on_purchase",
        readonly=False,
        string="Purchase Orders",
    )

    # ── Expiry warning setting ─────────────────────────────────────────────────
    stamp_expiry_warning_days = fields.Integer(
        related="company_id.stamp_expiry_warning_days",
        readonly=False,
        string="Expiry Warning (days)",
    )

    def action_save(self):
        self._validate_stamp_image()
        self._validate_signature_image()
        return {"type": "ir.actions.act_window_close"}

    def _validate_stamp_image(self):
        stamp_enabled = (
            self.print_stamp_on_quotation
            or self.print_stamp_on_invoice
            or self.print_stamp_on_delivery
            or self.print_stamp_on_purchase
        )
        if stamp_enabled and not self.company_stamp:
            raise ValidationError(
                _(
                    "You have enabled printing the stamp on one or more documents, "
                    "but no stamp image has been uploaded.\n\n"
                    "Please upload a stamp image or disable all 'Print Stamp On' options."
                )
            )

    def _validate_signature_image(self):
        signature_enabled = (
            self.print_signature_on_quotation
            or self.print_signature_on_invoice
            or self.print_signature_on_delivery
            or self.print_signature_on_purchase
        )
        if signature_enabled and not self.company_signature:
            raise ValidationError(
                _(
                    "You have enabled printing the signature on one or more documents, "
                    "but no signature image has been uploaded.\n\n"
                    "Please upload a signature image or disable all 'Print Signature On' options."
                )
            )

    def action_open_company_settings(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Company Settings"),
            "res_model": "res.company",
            "res_id": self.company_id.id,
            "view_mode": "form",
            "target": "current",
        }
