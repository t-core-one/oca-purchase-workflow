# Copyright 2024 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Purchase Warn Option",
    "summary": "Add Options to Purchase Warn Messages",
    "version": "15.0.1.0.0",
    "development_status": "Alpha",
    "category": "Inventory/Purchase",
    "website": "https://github.com/OCA/purchase-workflow",
    "author": "Moduon, Odoo Community Association (OCA)",
    "maintainers": ["Shide", "rafaelbn"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "auto_install": True,
    "depends": ["purchase", "base_warn_option"],
    "data": [
        "views/res_partner_views.xml",
        "views/product_template_views.xml",
    ],
}
