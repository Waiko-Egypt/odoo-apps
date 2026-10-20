{
    "name": "Company Stamp & Signature",
    "version": "19.0.1.0.3",
    "category": "Technical",
    "summary": "Stamp & signature on quotations, invoices, delivery notes and purchase orders — watermark, rotation, expiry, signatory label, expiry notifications.",
    "description": """
Company Stamp & Signature
=========================
Upload your company's official stamp and signature images to use in reports and documents.

Features:
- Upload company stamp and signature images
- Configure size (width/height in pixels)
- Set position (left, center, right)
- Adjust opacity (0.1 – 1.0)
- Stamp rotation (0 – 360 degrees)
- Signature rotation (0 – 360 degrees)
- Watermark mode (print stamp as page background)
- Stamp expiry date (auto-hides expired stamp)
- Signature expiry date (auto-hides expired signature)
- Expiry warning: daily cron notifies managers before stamp/signature expires
- Enable/disable per document type (quotation, invoice, delivery note, purchase order)
- Authorized Signatory label printed below the company signature
- Personal signature per employee (with per-employee signatory label)
- Audit log: all stamp/signature changes are tracked
- Security group to restrict stamp/signature management
    """,
    "author": "Eng. Mohamed Wally",
    "website": "https://mohamed-wally.com",
    "support": "info@mohamed-wally.com",
    "license": "OPL-1",
    "price": 14.00,
    "currency": "USD",
    "depends": ["base", "mail", "hr", "sale", "account", "stock", "purchase"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/cron.xml",
        "views/res_company_views.xml",
        "views/hr_employee_views.xml",
        "views/res_users_views.xml",
        "views/res_config_settings_views.xml",
        "views/stamp_wizard_views.xml",
        "report/report_base_stamp.xml",
        "report/report_sale_stamp.xml",
        "report/report_invoice_stamp.xml",
        "report/report_delivery_stamp.xml",
        "report/report_purchase_stamp.xml",
    ],
    "images": ["static/description/banner.png"],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "auto_install": False,
    "application": False,
}
