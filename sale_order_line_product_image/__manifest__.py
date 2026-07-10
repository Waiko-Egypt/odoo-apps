{
    "name": "Sale Order Line Product Image",
    "version": "13.0.1.0.0",
    "category": "Sales",
    "summary": "Show product image in sale order lines, quotation and invoice reports",
    "description": """
Sale Order Line Product Image – Odoo 13
========================================

Display product images in sale order lines, quotation reports, and invoice reports.

Features:
---------
* Product image column in sale order line tree view (optional)
* Product image in sale quotation / order PDF reports
* Product image in customer invoice PDF reports
* Company-level settings to enable/disable and control image dimensions
* Supports Community and Enterprise editions

Developer: Eng. Mohamed Wally
Website  : https://mohamed-wally.com
    """,
    "author": "Eng. Mohamed Wally",
    "website": "https://mohamed-wally.com",
    "depends": ["sale", "account"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/sale_order_views.xml",
        "views/report_templates.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
