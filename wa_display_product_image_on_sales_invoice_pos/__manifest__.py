{
    "name": "Display Product Image on Sales and Invoice",
    "version": "16.0.1.0.3",
    "category": "Sales",
    "summary": "Show product images in quotation, sale order, and invoice reports",
    "description": """
Display Product Image on Sales and Invoice - Odoo 16
=====================================================

Display product images in sale order lines, quotation reports, and invoice reports.

Features:
---------
* Product image in sale quotation / order PDF reports
* Product image in customer invoice PDF reports
* Company-level settings to enable/disable and control image dimensions
* Settings view designed for Odoo 16

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
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
