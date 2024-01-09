import pandas as pd


class StockImporter:
    """This class converts a list of stock data to a pandas dataframe.
    """

    def import_stock_data(self,
                          stock_data: str,
                          columns: list) -> pd.DataFrame:
        """Converts a list of stock data to a pandas dataframe."""
        stock_list = self._to_list(stock_data)

        for i, stock in enumerate(stock_list):
            if len(columns) != len(stock):
                raise ValueError(f'Number of columns in line {i + 1} does not '
                                 'match number of columns in stock data.')

        try:
            df = pd.DataFrame(stock_list, columns=columns)
            df = self._normalize_dataframe(df)
        except (ValueError, TypeError) as e:
            raise ValueError('Invalid stock data format.') from e

        return df

    def _normalize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Converts the dataframe to the correct data types."""
        df['date'] = pd.to_numeric(df['date'])
        df['price'] = pd.to_numeric(df['price'])

        return df

    def _to_list(self, stock_data: str) -> list:
        """Converts the stock data to a list of lists."""
        stock_data = stock_data.replace('\n', '')
        stock_list = stock_data.split(';')[:-1]
        stock_list = [stock.split(',') for stock in stock_list]

        for stock in stock_list:
            for i, column in enumerate(stock):
                stock[i] = column.strip()
            stock[1] = int(stock[1])
            stock[2] = float(stock[2])

        return stock_list
