import openpyxl

from configs.reporttypeenum import ReportType


def get_company(rec, avail_companies):
    return next([c, n] for (c, n) in avail_companies if n.lower() in rec.lower())


def get_price(price_str):
    if price_str:
        stripped_price = price_str.replace('$', '').replace(',', '')
        return float(stripped_price)
    else:
        return 0.0


def get_template(report_type, company):
    if report_type and company:
        match report_type:
            case ReportType.ORDERS.value:
                return openpyxl.load_workbook(f'./templates/orders/{company.lower()}_orders_template.xlsx')
            case ReportType.EOMS.value:
                return openpyxl.load_workbook(f'./templates/eoms/eoms_template.xlsx')