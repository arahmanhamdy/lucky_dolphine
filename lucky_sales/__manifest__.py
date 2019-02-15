{
    'name': 'Lucky Dolphin Sales',
    'depends': ['sale', 'purchase', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/parcel_view.xml',
        'views/crew_view.xml',
        'views/service_view.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/sale_order_batch_view.xml',
        # reports
        'reports/sale_order_xls_report_view.xml'
    ]
}
