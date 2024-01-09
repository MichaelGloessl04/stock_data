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

    stock_list = [
        ['Lenzing', 170447112, 34.75, 'EUR', 'Vienna'],
        ['Andritz', 170447131, 59.41, 'USD', 'New York'],
        ['EVN', 170447132, 28.55, 'EUR', 'Vienna'],
        ['EVN', 170447133, 31.18, 'USD', 'New York'],
    ]

    expected_columns = ['stock', 'date', 'price', 'currency', 'location']

    result = importer.import_stock_data(stock_data, expected_columns)

    assert isinstance(result, pd.DataFrame)
    assert result.columns.tolist() == expected_columns

    expected_rows = stock_data.count(';')
    assert len(result) == expected_rows

    assert result.values.tolist() == stock_list


def test_import_stock_data_with_invalid_columns():
    importer = StockImporter()

    stock_data = """
        Lenzing, 170447112, 34.75, EUR, Vienna;
        Andritz, 170447131, 59.41, USD, New York;
        EVN, 170447132, 28.55, EUR, Vienna;
        EVN, 170447133, 31.18, USD, New York;
    """

    invalid_columns = ['stock', 'date', 'price',
                       'currency', 'location', 'invalid']

    try:
        importer.import_stock_data(stock_data, invalid_columns)
        assert False
    except ValueError as e:
        assert str(e) == 'Number of columns in line 1 does not match number ' \
                         'of columns in stock data.'


def test_import_stock_data_with_invalid_stock_data():
    importer = StockImporter()

    invalid_stock_data = [
        ['invalid'],
        ('invalid'),
        {'invalid': 'invalid'},
        False,
        1,
        1.0,
        None
    ]

    columns = ['stock', 'date', 'price', 'currency', 'location']

    try:
        for stock_data in invalid_stock_data:
            importer.import_stock_data(stock_data, columns)
            assert False
    except TypeError as e:
        assert str(e) == 'stock_data must be a string. Got: ' \
                            f'{type(stock_data)}'
