import pandas as pd


class StockImporter:
    """This class converts a list of stock data to a pandas dataframe.
    """

    def import_stock_data(self,
                          stock_data: str,
                          columns: list) -> pd.DataFrame:
        """Converts a list of stock data to a pandas dataframe.
        """
        stock_list = self._to_list(stock_data)

        if len(columns) != len(stock_list[0]):
            raise ValueError("Number of columns does not match number of "
                             "columns in stock data.")

        df = pd.DataFrame(stock_list, columns=columns)
        return df

    def _to_list(self, stock_data: str) -> list:
        stock_data = stock_data.replace('\n', '')
        stock_list = stock_data.split(';')[:-1]
        stock_list = [stock.split(',') for stock in stock_list]
        for stock in stock_list:
            for i, column in enumerate(stock):
                stock[i] = column.strip()
            stock[1] = int(stock[1])
            stock[2] = float(stock[2])
        return stock_list
