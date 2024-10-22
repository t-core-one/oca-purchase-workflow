import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-procurement_purchase_no_grouping>=15.0dev,<15.1dev',
        'odoo-addon-procurement_purchase_sale_no_grouping>=15.0dev,<15.1dev',
        'odoo-addon-product_form_purchase_link>=15.0dev,<15.1dev',
        'odoo-addon-product_supplier_code_purchase>=15.0dev,<15.1dev',
        'odoo-addon-purchase_advance_payment>=15.0dev,<15.1dev',
        'odoo-addon-purchase_allowed_product>=15.0dev,<15.1dev',
        'odoo-addon-purchase_analytic_global>=15.0dev,<15.1dev',
        'odoo-addon-purchase_blanket_order>=15.0dev,<15.1dev',
        'odoo-addon-purchase_cancel_confirm>=15.0dev,<15.1dev',
        'odoo-addon-purchase_default_terms_conditions>=15.0dev,<15.1dev',
        'odoo-addon-purchase_delivery_split_date>=15.0dev,<15.1dev',
        'odoo-addon-purchase_deposit>=15.0dev,<15.1dev',
        'odoo-addon-purchase_deposit_analytic>=15.0dev,<15.1dev',
        'odoo-addon-purchase_discount>=15.0dev,<15.1dev',
        'odoo-addon-purchase_exception>=15.0dev,<15.1dev',
        'odoo-addon-purchase_fop_shipping>=15.0dev,<15.1dev',
        'odoo-addon-purchase_force_invoiced>=15.0dev,<15.1dev',
        'odoo-addon-purchase_fully_invoiced>=15.0dev,<15.1dev',
        'odoo-addon-purchase_fully_received>=15.0dev,<15.1dev',
        'odoo-addon-purchase_invoice_method>=15.0dev,<15.1dev',
        'odoo-addon-purchase_invoice_plan>=15.0dev,<15.1dev',
        'odoo-addon-purchase_last_price_info>=15.0dev,<15.1dev',
        'odoo-addon-purchase_line_reassign>=15.0dev,<15.1dev',
        'odoo-addon-purchase_location_by_line>=15.0dev,<15.1dev',
        'odoo-addon-purchase_manual_currency>=15.0dev,<15.1dev',
        'odoo-addon-purchase_merge>=15.0dev,<15.1dev',
        'odoo-addon-purchase_open_qty>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_analytic_search>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_approval_block>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_approved>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_general_discount>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_deep_sort>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_menu>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_original_date>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_price_history>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_price_history_discount>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_qty_to_receive>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_sequence>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_stock_available>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_no_zero_price>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_price_recalculation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation_brand>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation_classification>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation_forecast>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation_xlsx>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_qty_by_product_category>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_qty_change_no_recompute>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_supplierinfo_update>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_type>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_type_dashboard>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_uninvoiced_amount>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_weight_volume>=15.0dev,<15.1dev',
        'odoo-addon-purchase_partner_incoterm>=15.0dev,<15.1dev',
        'odoo-addon-purchase_partner_selectable_option>=15.0dev,<15.1dev',
        'odoo-addon-purchase_quick>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation_from_partner>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation_manual>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation_manual_split>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_percentage>=15.0dev,<15.1dev',
        'odoo-addon-purchase_reception_notify>=15.0dev,<15.1dev',
        'odoo-addon-purchase_reception_status>=15.0dev,<15.1dev',
        'odoo-addon-purchase_representative>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_cancel_confirm>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_department>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_exception>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_substate>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_to_requisition>=15.0dev,<15.1dev',
        'odoo-addon-purchase_requisition_grouped_by_procurement>=15.0dev,<15.1dev',
        'odoo-addon-purchase_requisition_order_remaining_qty>=15.0dev,<15.1dev',
        'odoo-addon-purchase_requisition_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_rfq_number>=15.0dev,<15.1dev',
        'odoo-addon-purchase_security>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_manual_currency>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_price_unit_sync>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_return_request>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_substate>=15.0dev,<15.1dev',
        'odoo-addon-purchase_tag>=15.0dev,<15.1dev',
        'odoo-addon-purchase_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_total_ordered_qty>=15.0dev,<15.1dev',
        'odoo-addon-purchase_triple_discount>=15.0dev,<15.1dev',
        'odoo-addon-purchase_v12_control_menu>=15.0dev,<15.1dev',
        'odoo-addon-purchase_warn_message>=15.0dev,<15.1dev',
        'odoo-addon-purchase_warn_option>=15.0dev,<15.1dev',
        'odoo-addon-purchase_work_acceptance>=15.0dev,<15.1dev',
        'odoo-addon-purchase_work_acceptance_evaluation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_work_acceptance_invoice_plan>=15.0dev,<15.1dev',
        'odoo-addon-purchase_work_acceptance_late_fines>=15.0dev,<15.1dev',
        'odoo-addon-purchase_work_acceptance_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-sale_purchase_force_vendor>=15.0dev,<15.1dev',
        'odoo-addon-sale_purchase_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-stock_move_purchase_price_update>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_batch_purchase_price_update>=15.0dev,<15.1dev',
        'odoo-addon-subcontracted_service>=15.0dev,<15.1dev',
        'odoo-addon-supplier_calendar>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
