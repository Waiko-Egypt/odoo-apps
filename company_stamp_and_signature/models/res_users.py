from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    # ── Toggle ────────────────────────────────────────────────────────────────
    use_personal_signature = fields.Boolean(
        string="Use My Personal Signature on Documents",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
    )

    # ── Image ─────────────────────────────────────────────────────────────────
    employee_signature = fields.Binary(
        string="My Signature",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
        help="Upload your personal signature. It will replace the company "
        "signature on documents where you are the responsible salesperson.",
    )
    employee_signature_filename = fields.Char(
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
    )

    # ── Display properties ────────────────────────────────────────────────────
    employee_signature_width = fields.Integer(
        string="Width (px)",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
    )
    employee_signature_height = fields.Integer(
        string="Height (px)",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
    )
    employee_signature_opacity = fields.Float(
        string="Opacity (0.1 – 1.0)",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
        digits=(3, 2),
    )
    employee_signature_position = fields.Selection(
        selection=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        string="Position",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
    )
    employee_signature_rotation = fields.Integer(
        string="Rotation (°)",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
    )
    employee_signatory_label = fields.Char(
        string="Signatory Label",
        compute="_compute_personal_signature_fields",
        inverse="_inverse_personal_signature_fields",
        readonly=False,
        help="Label printed below your signature (e.g. 'Sales Manager'). "
        "Leave empty to use the company default.",
    )

    @api.depends(
        "employee_id.use_personal_signature",
        "employee_id.employee_signature",
        "employee_id.employee_signature_filename",
        "employee_id.employee_signature_width",
        "employee_id.employee_signature_height",
        "employee_id.employee_signature_opacity",
        "employee_id.employee_signature_position",
        "employee_id.employee_signature_rotation",
        "employee_id.employee_signatory_label",
    )
    def _compute_personal_signature_fields(self):
        for user in self:
            emp = user.employee_id.sudo() if user.employee_id else False
            if emp:
                user.use_personal_signature = emp.use_personal_signature
                user.employee_signature = emp.employee_signature
                user.employee_signature_filename = emp.employee_signature_filename
                user.employee_signature_width = emp.employee_signature_width
                user.employee_signature_height = emp.employee_signature_height
                user.employee_signature_opacity = emp.employee_signature_opacity
                user.employee_signature_position = emp.employee_signature_position
                user.employee_signature_rotation = emp.employee_signature_rotation
                user.employee_signatory_label = emp.employee_signatory_label
            else:
                user.use_personal_signature = False
                user.employee_signature = False
                user.employee_signature_filename = False
                user.employee_signature_width = 150
                user.employee_signature_height = 80
                user.employee_signature_opacity = 1.0
                user.employee_signature_position = "right"
                user.employee_signature_rotation = 0
                user.employee_signatory_label = False

    def _inverse_personal_signature_fields(self):
        for user in self:
            if user.employee_id:
                emp = user.employee_id.sudo()
                emp.use_personal_signature = user.use_personal_signature
                emp.employee_signature = user.employee_signature
                emp.employee_signature_filename = user.employee_signature_filename
                emp.employee_signature_width = user.employee_signature_width
                emp.employee_signature_height = user.employee_signature_height
                emp.employee_signature_opacity = user.employee_signature_opacity
                emp.employee_signature_position = user.employee_signature_position
                emp.employee_signature_rotation = user.employee_signature_rotation
                emp.employee_signatory_label = user.employee_signatory_label
