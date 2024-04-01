import sys

from configs.reporttypeenum import ReportType
from reportgenerators.orders import generate_orders
from reportgenerators.eoms import generate_eoms


def main(report = None, companies = []):
    if report and companies:
        match report:
            case ReportType.ORDERS.value:
                generate_orders(companies[0])
            case ReportType.EOMS.value:
                generate_eoms(companies)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        report = sys.argv[1]
        companies = sys.argv[2:]

        main(report, companies)
