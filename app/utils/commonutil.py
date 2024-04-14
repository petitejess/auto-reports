import os
import shutil
import openpyxl

from configs.dirconfigenum import DirPath
from configs.reporttypeenum import ReportType


def get_company(rec, avail_companies):
    return next([c, n] for (c, n) in avail_companies if n.lower() in rec.lower())


def get_price(price_str):
    if price_str:
        stripped_price = price_str.replace("$", "").replace(",", "")
        return float(stripped_price)
    else:
        return 0.0


def get_template(report_type, company):
    if report_type and company:
        match report_type:
            case ReportType.ORDERS.value:
                return openpyxl.load_workbook(DirPath.ORDER_TEMPLATE.value.format(company=company.lower()))
            case ReportType.EOMS.value:
                return openpyxl.load_workbook(DirPath.EOMS_TEMPLATE.value)


def move_to_archive(output_path, archive_destination, file_ext):
    if os.path.exists(output_path):
        sequence = 1
        new_archive_path = f"{archive_destination} ({sequence}){file_ext}"

        # Rename file with sequence number
        while os.path.exists(new_archive_path):
            sequence += 1
            new_archive_path = f"{archive_destination} ({sequence}){file_ext}"

        # Move existing file to archive
        shutil.move(output_path, new_archive_path)
        print(f"Existing file moved to {new_archive_path}")
