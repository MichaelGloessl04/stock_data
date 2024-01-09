import pandas as pd
from stock_importer import StockImporter


def test_init():
    importer = StockImporter()

    assert isinstance(importer, StockImporter)


def test_import_stock_data():
    importer = StockImporter()

    stock_data = """
        Lenzing, 170447112, 34.75, EUR, Vienna;
        Andritz, 170447131, 59.41, USD, New York;
        EVN, 170447132, 28.55, EUR, Vienna;
        EVN, 170447133, 31.18, USD, New York;
    """

    expected_columns = ["stock", "date", "price", "currency", "location"]

    result = importer.import_stock_data(stock_data, expected_columns)

    assert isinstance(result, pd.DataFrame)
    assert result.columns.tolist() == expected_columns

    expected_rows = stock_data.count(";")
    assert len(result) == expected_rows
