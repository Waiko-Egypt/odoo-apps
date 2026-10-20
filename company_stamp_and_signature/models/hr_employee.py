from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # ── Personal Signature ──────────────────────────────────────────────────
    use_personal_signature = fields.Boolean(
        string="Use Personal Signature on Documents",
        default=True,
        help="When enabled, and a personal signature image is uploaded, "
        "this employee's own signature is printed on quotations and "
        "invoices instead of the company signature "
        "whenever this employee is the responsible salesperson "
        "(i.e. logged in when the document is created).",
    )
    employee_signature = fields.Binary(
        string="Personal Signature",
        attachment=True,
    )
    employee_signature_filename = fields.Char(
        string="Signature Filename",
    )
    employee_signature_width = fields.Integer(
        string="Signature Width (px)",
        default=150,
    )
    employee_signature_height = fields.Integer(
        string="Signature Height (px)",
        default=80,
    )
    employee_signature_opacity = fields.Float(
        string="Signature Opacity",
        default=1.0,
        digits=(3, 2),
    )
    employee_signature_position = fields.Selection(
        selection=[
            ("left", "Left"),
            ("center", "Center"),
            ("right", "Right"),
        ],
        string="Signature Position",
        default="right",
    )
    employee_signature_rotation = fields.Integer(
        string="Signature Rotation (°)",
        default=0,
        help="Rotation angle for the personal signature image in degrees (0-360).",
    )
    # ── Authorized Signatory Label (per employee) ─────────────────────────────
    employee_signatory_label = fields.Char(
        string="Signatory Label",
        help="Override label printed below this employee's personal signature "
        "(e.g. 'Sales Manager'). Leave empty to use the company default.",
    )

    # ── Validation ────────────────────────────────────────────────────────────
    @api.constrains("employee_signature_rotation")
    def _check_employee_signature_rotation(self):
        for rec in self:
            if not (0 <= rec.employee_signature_rotation <= 360):
                raise ValidationError(
                    _("Signature rotation must be between 0 and 360 degrees.")
                )

    @api.constrains("employee_signature_opacity")
    def _check_employee_signature_opacity(self):
        for rec in self:
            if not (0.1 <= rec.employee_signature_opacity <= 1.0):
                raise ValidationError(
                    _("Signature opacity must be between 0.1 and 1.0.")
                )

    @api.constrains("employee_signature_width", "employee_signature_height")
    def _check_employee_signature_dimensions(self):
        for rec in self:
            if rec.employee_signature_width < 10 or rec.employee_signature_height < 10:
                raise ValidationError(
                    _("Signature width and height must be at least 10 pixels.")
                )

    def _get_document_signature(self):
        """Return the personal signature data to print for this employee, or
        False if this employee has no usable personal signature configured
        (in which case callers should fall back to the company signature).

        Returns a dict with keys:
          image, width, height, opacity, position, rotation, label
        """
        self.ensure_one()
        if self.use_personal_signature and self.employee_signature:
            company = self.company_id
            label = self.employee_signatory_label or (
                company.authorized_signatory_label
                if company.show_signatory_label
                else False
            )
            return {
                "image": self.employee_signature,
                "width": self.employee_signature_width,
                "height": self.employee_signature_height,
                "opacity": self.employee_signature_opacity,
                "position": self.employee_signature_position,
                "rotation": self.employee_signature_rotation,
                "label": label,
            }
        return False
