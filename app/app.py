import sys

# from enums.reporttypeenum import ReportType
# from reportgenerators.orders import generate_orders
# from reportgenerators.eoms import generate_eoms


def main(report=None):
    if report:
        # match report:
        #     case ReportType.ORDERS.value:
        #         generate_orders()
        #     case ReportType.EOMS.value:
        #         generate_eoms()

        print(report)


if __name__ == "__main__":

    print(sys.argv)

    if len(sys.argv) > 1:
        report = sys.argv[1]

        print(report)

        main(report)
