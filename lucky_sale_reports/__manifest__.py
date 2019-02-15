{
    'name': 'Lucky Dolphin Sale Reports',
    'summary': 'Lucky Dolphin Sale Reports',

    'description': """
        This module add the following features in sale module
            1- Xls report for sale order.\n
    """,
    'depends': ['sale', 'report_xlsx'],
    'data': [
        # reports
        'reports/sale_order_xls_report_view.xml'
    ],

    'installable': True,
    'auto_install': False,
    'sequence': 1
}
