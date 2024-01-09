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

    result = importer.import_stock_data(stock_data)

    assert isinstance(result, pd.DataFrame)

    expected_columns = ["stock", "date", "price", "currency", "location"]
    assert result.columns.tolist() == expected_columns

    expected_rows = len(stock_data)
    assert len(result) == expected_rows
