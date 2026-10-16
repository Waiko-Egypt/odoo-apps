{
    "name": "Display Product Image on Sales and Invoice",
    "version": "17.0.1.0.2",
    "category": "Sales",
    "summary": "Show product images in quotation, sale order, and invoice reports",
    "description": """
Display Product Image on Sales and Invoice - Odoo 17
=====================================================

Display product images in sale order lines, quotation reports, and invoice reports.

Features:
---------
* Product image in quotation / sale-order lines and PDF reports
* Product image in customer-invoice lines and PDF reports
* Company-level settings to enable/disable and control image dimensions
* Native Odoo 17 settings view
* Safe initialization for existing companies and report image sizes

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
    "post_init_hook": "post_init_hook",
    "license": "LGPL-3",
}
