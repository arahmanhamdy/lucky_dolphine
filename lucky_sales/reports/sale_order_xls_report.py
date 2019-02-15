# -*- coding: utf-8 -*-
from odoo import models, api, fields, _


class SaleForecastingReportXls(models.AbstractModel):
    _inherit = 'report.report_xlsx.abstract'
    _name = 'report.lucky_sales.sale_order_xls_report'

    def generate_xlsx_report(self, workbook, data, sale_orders):
        worksheet = workbook.add_worksheet("Sale Order Report")
        f1 = workbook.add_format({'bold': True, 'font_color': 'black', })
        f2 = workbook.add_format({'font_color': 'black', })
        report_line_number = 2
        line_number = 0
        for sale_order in sale_orders:
            # partner address
            partner_address = ''
            if sale_order.partner_id.zip:
                partner_address += str(sale_order.partner_id.zip) + ' '
            if sale_order.partner_id.city:
                partner_address += str(sale_order.partner_id.city) + ' , '
            if sale_order.partner_id.state_id:
                partner_address += str(sale_order.partner_id.state_id.name)

            worksheet.write(report_line_number, 5, sale_order.partner_id.name, f2)
            report_line_number += 1
            worksheet.write(report_line_number, 5, sale_order.partner_id.street, f2)
            report_line_number += 1
            worksheet.write(report_line_number, 5, partner_address, f2)
            report_line_number += 1
            worksheet.write(report_line_number, 5, sale_order.partner_id.country_id.name, f2)
            if sale_order.partner_id.vat:
                worksheet.write(report_line_number, 5, "Tax ID :" + sale_order.partner_id.vat, f2)
                report_line_number += 1

            # order details
            if sale_order.state in ['draft', 'sent']:
                worksheet.write(report_line_number, 1, "Quotation #" + sale_order.name, f1)
                report_line_number += 1

            elif sale_order.state not in ['draft', 'sent']:
                worksheet.write(report_line_number, 1, "Order #" + sale_order.name, f1)
                report_line_number += 1

            if sale_order.client_order_ref:
                worksheet.write(report_line_number, 1, "Your Reference : ", f2)

            if sale_order.confirmation_date and sale_order.state not in ['draft', 'sent']:
                worksheet.write(report_line_number, 2,
                                "Date Ordered : ", f2)

            if sale_order.date_order and sale_order.state in ['draft', 'sent']:
                worksheet.write(report_line_number, 3,
                                "Quotation Date : ", f2)

            if sale_order.user_id.name:
                worksheet.write(report_line_number, 4, "Salesperson : ", f2)

            if sale_order.payment_term_id.name:
                worksheet.write(report_line_number, 5, "Payment Terms : ", f2)

            if sale_order.validity_date and sale_order.state in ['draft', 'sent']:
                worksheet.write(report_line_number, 6,
                                "Expiration Date : ", f2)

            report_line_number += 1

            if sale_order.client_order_ref:
                worksheet.write(report_line_number, 1, sale_order.client_order_ref, f2)

            if sale_order.confirmation_date and sale_order.state not in ['draft', 'sent']:
                worksheet.write(report_line_number, 2,
                                fields.Datetime.to_string(sale_order.confirmation_date), f2)

            if sale_order.date_order and sale_order.state in ['draft', 'sent']:
                worksheet.write(report_line_number, 3,
                                fields.Datetime.to_string(sale_order.date_order), f2)

            if sale_order.user_id.name:
                worksheet.write(report_line_number, 4, sale_order.user_id.name, f2)

            if sale_order.payment_term_id.name:
                worksheet.write(report_line_number, 5, sale_order.payment_term_id.name, f2)

            if sale_order.validity_date and sale_order.state in ['draft', 'sent']:
                worksheet.write(report_line_number, 6,
                                fields.Date.to_string(sale_order.validity_date), f2)
            report_line_number += 1
            # products in lines
            report_line_number = line_number + 2
