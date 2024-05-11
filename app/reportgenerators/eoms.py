from datetime import datetime
import json

import pandas as pd
from app.utils.dirutil import read_config
from enums.companynameenum import CompanyName
from enums.dirconfigenum import DirPath
from enums.reporttypeenum import ReportType
from utils.commonutil import get_eom_date, get_price, get_template, move_to_archive


def generate_eoms():
    print(f"｡:.ﾟヽ(´∀`｡)ﾉﾟ.:｡+ﾟ")
    print(f"ﾟ+｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡+ﾟ ~~ Generating end of month statements...")
    print(f"｡:.ﾟヽ(´∀`｡)ﾉﾟ.:｡+ﾟ")

    avail_companies = [
        CompanyName.AHI,
        CompanyName.CHA,
        CompanyName.COS,
        CompanyName.EST,
        CompanyName.HAL,
        CompanyName.JUR,
        CompanyName.LAP,
        CompanyName.LOR,
        CompanyName.LVM,
        CompanyName.NAT,
        CompanyName.SEA,
        CompanyName.SEN,
        CompanyName.SIS,
        CompanyName.TRI,
        CompanyName.ULT,
    ]

    file_config = read_config(DirPath.INCONF.value)
    lookup_config = read_config(DirPath.EOMS_LOOKUP.value)
    file_input = DirPath.IN_EOMS.value

    input_delimiter = file_config["myob"]["delimiter"]
    input_header = file_config["myob"]["header"]
    sheetname = file_config["excel"]["eoms"]["sheetname"]
    company_col = file_config["excel"]["eoms"]["company_col"]
    current_date_loc = file_config["excel"]["eoms"]["current_date_loc"]
    lookup = lookup_config["lookup"]

    def filter_companies(df, comp_name=None):
        matched_companies = []
        if comp_name:
            df_subset = df[df[company_col].str.contains(comp_name, case=False)]
            matched_companies.append(df_subset)
        else:
            for [_, company] in avail_companies:
                df_subset = df[df[company_col].str.contains(company, case=False)]
                matched_companies.append(df_subset)

        return pd.concat(matched_companies)

    df = pd.read_table(file_input, delimiter=input_delimiter, header=input_header)

    company_df = df.copy()
    company_df = filter_companies(company_df)
    company_df = company_df[[company_col, "Invoice No.", "Date", "Customer PO", "Total", "Tax Amount"]]

    company_df["Total"] = company_df["Total"].apply(get_price)
    company_df["Tax Amount"] = company_df["Tax Amount"].apply(get_price)

    company_df.fillna("NaN", inplace=True)

    company_df = company_df.groupby([company_col, "Invoice No.", "Date", "Customer PO"], sort=True).sum()

    company_df["Invoice Total"] = company_df["Total"] + company_df["Tax Amount"]
    company_df = company_df.reset_index()

    sum_df = company_df.groupby(company_col, sort=True).sum()
    sum_df["Company Total"] = sum_df["Invoice Total"]
    sum_df = sum_df.reset_index()
    sum_df = sum_df[[company_col, "Company Total"]]

    final_df = pd.merge(company_df, sum_df, how="inner", on=company_col)

    # Metadata
    last_date = get_eom_date(datetime.now())
    for [_, company] in avail_companies:
        comp_df = filter_companies(final_df, company)

        if not comp_df.empty:
            comp_df = comp_df.sort_values(by="Date", ascending=True)
            template = get_template(ReportType.EOMS.value)
            sheet = template[sheetname]

            sheet[current_date_loc] = last_date

            cdf_date = comp_df["Date"]
            cdf_invoice = comp_df["Invoice No."]
            cdf_customer = comp_df["Co./Last Name"]
            cdf_po = comp_df["Customer PO"]
            cdf_total = comp_df["Invoice Total"]
            cdf_balance = comp_df["Company Total"]

            for row_num, (date_val, invoice_val, customer_val, po_val, charge_val, balance_val) in enumerate(
                zip(cdf_date, cdf_invoice, cdf_customer, cdf_po, cdf_total, cdf_balance),
                start=lookup["template"]["start_row"],
            ):
                customer_po = customer_val + f"/PO#{po_val}" if po_val else customer_val

                sheet[f'{lookup["template"]["date"]}{row_num}'] = date_val
                sheet[f'{lookup["template"]["invoice"]}{row_num}'] = invoice_val
                sheet[f'{lookup["template"]["customer"]}{row_num}'] = customer_po
                sheet[f'{lookup["template"]["charges"]}{row_num}'] = charge_val
                sheet[f'{lookup["template"]["balance"]}{row_num}'] = balance_val

            # Output
            new_filename = f"{company}_Statement_{last_date.strftime('%d-%b-%Y')}"
            # output_path = f"./reports/{new_filename}"
            output_path = f"{DirPath.OUT_EOMS.value}{new_filename}" + ".xlsx"

            # Move to archive if file already exists
            archive_destination = f"{DirPath.OUT_EOMS_ARCHIVE.value}{new_filename}"
            move_to_archive(output_path, archive_destination, ".xlsx")

            # Save the file
            template.save(output_path)

            print(f"Data saved to {output_path}")
