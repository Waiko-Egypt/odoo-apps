{
    "name": "Display Product Image on Sales and Invoice",
    "version": "17.0.1.0.3",
    "category": "Sales",
    "summary": "Show product images in quotation, sale order, invoice forms and PDF reports",
    "description": """
Display Product Image on Sales and Invoice - Odoo 17
=====================================================

Automatically display each product's image inside Quotations, Sale Orders,
Customer Invoices, and their PDF reports.

Features:
---------
* Product thumbnail column in Quotation / Sale Order form tree view
* Product thumbnail column in Customer Invoice / Vendor Bill form tree view
* Product image column in Sale Order / Quotation PDF report
  (sale.report_saleorder_document)
* Product image column in Customer Invoice PDF report
  (account.report_invoice_document)
* Company-level toggle to enable / disable images in PDF reports
* Configurable image width and height (in pixels) per company
* Multi-company support — settings stored on res.company
* Native Odoo 17 settings page under Settings > Product Images
* Uses standard Odoo product images (image_128) — no extra upload needed
* Safe post-init hook initializes dimensions for existing companies
* Migration script repairs null / zero dimensions on upgrade
* Zero third-party dependencies — works with standard Sales + Invoicing

Configuration:
--------------
Settings > Product Images > Show Product Image in Reports (toggle)
Settings > Product Images > Product Image Width  (px, default 40)
Settings > Product Images > Product Image Height (px, default 40)

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
    "web_icon": "wa_display_product_image_on_sales_invoice_pos/static/description/icon.png",
    "post_init_hook": "post_init_hook",
    "license": "LGPL-3",
}
