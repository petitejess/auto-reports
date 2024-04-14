import sys

from configs.reporttypeenum import ReportType
from reportgenerators.orders import generate_orders
from reportgenerators.eoms import generate_eoms


def main(report=None):
    if report:
        match report:
            case ReportType.ORDERS.value:
                generate_orders()
            case ReportType.EOMS.value:
                generate_eoms()


if __name__ == "__main__":

    if len(sys.argv) > 1:
        report = sys.argv[1]

        main(report)
