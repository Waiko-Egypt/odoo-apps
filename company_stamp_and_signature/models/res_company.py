from datetime import timedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    # ── Stamp ────────────────────────────────────────────────────────────────
    company_stamp = fields.Binary(
        string="Company Stamp", attachment=True, tracking=True
    )
    company_stamp_filename = fields.Char(string="Stamp Filename")
    stamp_width = fields.Integer(string="Stamp Width (px)", default=150)
    stamp_height = fields.Integer(string="Stamp Height (px)", default=150)
    stamp_opacity = fields.Float(string="Stamp Opacity", default=1.0, digits=(3, 2))
    stamp_position = fields.Selection(
        selection=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        string="Stamp Position",
        default="right",
    )
    # ── Advanced Stamp Settings ───────────────────────────────────────────────
    stamp_rotation = fields.Integer(
        string="Stamp Rotation (°)",
        default=0,
        help="Rotation angle for the stamp image in degrees (0-360). "
        "Example: 45° gives a diagonal look.",
    )
    stamp_as_watermark = fields.Boolean(
        string="Use Stamp as Watermark",
        default=False,
        help="When enabled, the stamp is printed as a large background "
        "watermark on the page instead of the normal corner position.",
    )
    stamp_expiry_date = fields.Date(
        string="Stamp Expiry Date",
        tracking=True,
        help="After this date the stamp will no longer appear on printed documents. "
        "Leave empty for no expiry.",
    )
    stamp_is_expired = fields.Boolean(
        string="Stamp Is Expired",
        compute="_compute_stamp_is_expired",
        # Not stored — evaluated at runtime so the stamp automatically
        # disappears on the correct calendar date without any manual action.
    )

    # ── Stamp print options ───────────────────────────────────────────────────
    print_stamp_on_quotation = fields.Boolean(
        string="Print Stamp on Quotations", default=False, tracking=True
    )
    print_stamp_on_invoice = fields.Boolean(
        string="Print Stamp on Invoices", default=False, tracking=True
    )
    print_stamp_on_delivery = fields.Boolean(
        string="Print Stamp on Delivery Notes", default=False, tracking=True
    )
    print_stamp_on_purchase = fields.Boolean(
        string="Print Stamp on Purchase Orders", default=False, tracking=True
    )

    # ── Signature ────────────────────────────────────────────────────────────
    company_signature = fields.Binary(
        string="Company Signature", attachment=True, tracking=True
    )
    company_signature_filename = fields.Char(string="Signature Filename")
    signature_width = fields.Integer(string="Signature Width (px)", default=150)
    signature_height = fields.Integer(string="Signature Height (px)", default=80)
    signature_opacity = fields.Float(
        string="Signature Opacity", default=1.0, digits=(3, 2)
    )
    signature_position = fields.Selection(
        selection=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        string="Signature Position",
        default="right",
    )
    signature_rotation = fields.Integer(
        string="Signature Rotation (°)",
        default=0,
        help="Rotation angle for the signature image in degrees (0-360).",
    )
    signature_expiry_date = fields.Date(
        string="Signature Expiry Date",
        tracking=True,
        help="After this date the signature will no longer appear on printed documents. "
        "Leave empty for no expiry.",
    )
    signature_is_expired = fields.Boolean(
        string="Signature Is Expired",
        compute="_compute_signature_is_expired",
    )

    # ── Authorized Signatory Label ────────────────────────────────────────────
    authorized_signatory_label = fields.Char(
        string="Authorized Signatory Label",
        default="Authorized Signatory",
        help="Text printed below the company signature on documents, "
        "e.g. 'Authorized Signatory' or 'General Manager'.",
    )
    show_signatory_label = fields.Boolean(
        string="Show Signatory Label",
        default=False,
        help="When enabled, the authorized signatory label is printed below "
        "the signature on documents.",
    )

    # ── Signature print options ───────────────────────────────────────────────
    print_signature_on_quotation = fields.Boolean(
        string="Print Signature on Quotations", default=False, tracking=True
    )
    print_signature_on_invoice = fields.Boolean(
        string="Print Signature on Invoices", default=False, tracking=True
    )
    print_signature_on_delivery = fields.Boolean(
        string="Print Signature on Delivery Notes", default=False, tracking=True
    )
    print_signature_on_purchase = fields.Boolean(
        string="Print Signature on Purchase Orders", default=False, tracking=True
    )

    # ── Expiry warning ────────────────────────────────────────────────────────
    stamp_expiry_warning_days = fields.Integer(
        string="Expiry Warning (days)",
        default=7,
        help="Send a chatter notification to Stamp & Signature Managers this many "
        "days before the stamp or signature expires. Set to 0 to disable.",
    )

    # ── Computed ──────────────────────────────────────────────────────────────
    @api.depends("stamp_expiry_date")
    def _compute_stamp_is_expired(self):
        today = fields.Date.today()
        for rec in self:
            rec.stamp_is_expired = bool(
                rec.stamp_expiry_date and rec.stamp_expiry_date < today
            )

    @api.depends("signature_expiry_date")
    def _compute_signature_is_expired(self):
        today = fields.Date.today()
        for rec in self:
            rec.signature_is_expired = bool(
                rec.signature_expiry_date and rec.signature_expiry_date < today
            )

    # ── Validation ────────────────────────────────────────────────────────────
    @api.constrains("stamp_opacity")
    def _check_stamp_opacity(self):
        for rec in self:
            if not (0.1 <= rec.stamp_opacity <= 1.0):
                raise ValidationError(_("Stamp opacity must be between 0.1 and 1.0."))

    @api.constrains("signature_opacity")
    def _check_signature_opacity(self):
        for rec in self:
            if not (0.1 <= rec.signature_opacity <= 1.0):
                raise ValidationError(
                    _("Signature opacity must be between 0.1 and 1.0.")
                )

    @api.constrains("stamp_width", "stamp_height")
    def _check_stamp_dimensions(self):
        for rec in self:
            if rec.stamp_width < 10 or rec.stamp_height < 10:
                raise ValidationError(
                    _("Stamp width and height must be at least 10 pixels.")
                )

    @api.constrains("signature_width", "signature_height")
    def _check_signature_dimensions(self):
        for rec in self:
            if rec.signature_width < 10 or rec.signature_height < 10:
                raise ValidationError(
                    _("Signature width and height must be at least 10 pixels.")
                )

    @api.constrains("stamp_rotation")
    def _check_stamp_rotation(self):
        for rec in self:
            if not (0 <= rec.stamp_rotation <= 360):
                raise ValidationError(
                    _("Stamp rotation must be between 0 and 360 degrees.")
                )

    @api.constrains("signature_rotation")
    def _check_signature_rotation(self):
        for rec in self:
            if not (0 <= rec.signature_rotation <= 360):
                raise ValidationError(
                    _("Signature rotation must be between 0 and 360 degrees.")
                )

    # ── Cron: stamp/signature expiry warning ──────────────────────────────────
    def _cron_check_stamp_expiry(self):
        """Daily cron: notify Stamp & Signature Managers when a company stamp or
        signature is about to expire (exactly stamp_expiry_warning_days days away).
        Posts a chatter note on the company record and mentions all managers.
        """
        today = fields.Date.today()
        group = self.env.ref(
            "company_stamp_and_signature.group_stamp_manager",
            raise_if_not_found=False,
        )
        manager_partner_ids = group.users.mapped("partner_id").ids if group else []

        for company in self.sudo().search([]):
            days = company.stamp_expiry_warning_days
            if not days or days <= 0:
                continue
            threshold = today + timedelta(days=days)
            msgs = []

            if company.stamp_expiry_date and company.stamp_expiry_date == threshold:
                msgs.append(
                    _(
                        "<b>⚠ Stamp Expiry Warning</b><br/>"
                        "The company stamp will expire on <b>%(date)s</b> "
                        "(%(days)d day(s) from today).<br/>"
                        "Please upload a new stamp image or extend the expiry date."
                    )
                    % {"date": company.stamp_expiry_date, "days": days}
                )

            if (
                company.signature_expiry_date
                and company.signature_expiry_date == threshold
            ):
                msgs.append(
                    _(
                        "<b>⚠ Signature Expiry Warning</b><br/>"
                        "The company signature will expire on <b>%(date)s</b> "
                        "(%(days)d day(s) from today).<br/>"
                        "Please upload a new signature image or extend the expiry date."
                    )
                    % {"date": company.signature_expiry_date, "days": days}
                )

            if msgs:
                company.message_post(
                    body="<br/><br/>".join(msgs),
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=manager_partner_ids,
                )
