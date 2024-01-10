from visualization import plot_stock_data
from stock_importer import StockImporter

# data generated by chat gpt based of the given example
STOCKDATA = """
    Lenzing, 170447112, 34.75, EUR, Vienna;
    Andritz, 170447131, 59.41, USD, New York;
    EVN, 170447132, 28.55, EUR, Vienna;
    EVN, 170447133, 31.18, USD, New York;
    Lenzing, 170447134, 36.20, USD, Frankfurt;
    Andritz, 170447135, 58.80, EUR, Paris;
    EVN, 170447136, 29.75, USD, London;
    EVN, 170447137, 32.45, EUR, Frankfurt;
    Lenzing, 170447138, 35.10, USD, Vienna;
    Andritz, 170447139, 60.15, EUR, New York;
    EVN, 170447140, 28.90, USD, Paris;
    EVN, 170447141, 31.75, EUR, London;
    Lenzing, 170447142, 34.50, USD, New York;
    Andritz, 170447143, 59.80, EUR, Vienna;
    EVN, 170447144, 28.25, USD, Frankfurt;
    EVN, 170447145, 30.90, EUR, Paris;
    Lenzing, 170447146, 37.05, USD, London;
    Andritz, 170447147, 58.20, EUR, Frankfurt;
    EVN, 170447148, 29.45, USD, Vienna;
    EVN, 170447149, 32.15, EUR, New York;
    Lenzing, 170447150, 35.80, USD, Paris;
    Andritz, 170447151, 61.00, EUR, London;
    EVN, 170447152, 28.60, USD, Frankfurt;
    EVN, 170447153, 31.40, EUR, Vienna;
    Lenzing, 170447154, 34.10, USD, New York;
    Andritz, 170447155, 59.10, EUR, Paris;
    EVN, 170447156, 28.80, USD, London;
    EVN, 170447157, 31.90, EUR, Frankfurt;
    Lenzing, 170447158, 36.50, USD, Vienna;
    Andritz, 170447159, 58.50, EUR, New York;
    EVN, 170447160, 29.30, USD, Paris;
    EVN, 170447161, 32.25, EUR, London;
    Lenzing, 170447162, 33.70, USD, New York;
    Andritz, 170447163, 60.50, EUR, Vienna;
    EVN, 170447164, 28.40, USD, Frankfurt;
    EVN, 170447165, 30.70, EUR, Paris;
    Lenzing, 170447166, 35.40, USD, London;
    Andritz, 170447167, 59.70, EUR, Frankfurt;
    EVN, 170447168, 29.60, USD, Vienna;
    EVN, 170447169, 31.60, EUR, New York;
    Lenzing, 170447170, 34.90, USD, Paris;
    Andritz, 170447171, 58.00, EUR, London;
    EVN, 170447172, 28.75, USD, Frankfurt;
    EVN, 170447173, 31.10, EUR, Vienna.
"""

COLUMNS = ['stock', 'date', 'price', 'currency', 'location']


def main():
    stock_importer = StockImporter()
    df = stock_importer.import_stock_data(STOCKDATA, COLUMNS)
    plot_stock_data(df)


if __name__ == '__main__':
    main()
