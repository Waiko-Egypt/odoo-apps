# -*- coding: utf-8 -*-
{
    "name": "Product Warranty Management",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "summary": "Warranty management used to manage warranty of product",
    "description": """
Product Warranty Management
============================
A warranty period (months / years) can be set for products.
The warranty starts on the invoice date when the invoice is posted, and its
start and end dates are printed on the customer invoice.

Features:
---------
* Add warranty duration and period type (Months/Years) on product form.
* Display warranty column in Sale Order and Invoice reports.
* Automatically calculate warranty start and end dates when an invoice is posted.
* Warranty start date = Customer invoice date.
* Warranty end date = Start date + warranty duration.
* Compatible with Odoo 17.0 Community and Enterprise editions.
    """,
    "author": "Eng. Mohamed Wally",
    "website": "https://mohamed-wally.com",
    "license": "LGPL-3",
    "depends": [
        "product",
        "sale_management",
        "account",
    ],
    "data": [
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        "report/sale_report_templates.xml",
        "report/invoice_report_templates.xml",
    ],
    "assets": {
        "web.report_assets_common": [
            "wa_product_warranty_mgmt/static/src/scss/report_warranty.scss",
        ],
    },
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
