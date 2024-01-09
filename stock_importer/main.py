import pandas as pd


class StockImporter:
    """This class converts a list of stock data to a pandas dataframe.
    """

    def import_stock_data(self,
                          stock_data: str,
                          columns: list) -> pd.DataFrame:
        """Converts a list of stock data to a pandas dataframe.
        """
        stock_data = stock_data.replace('\n', '')
        stock_data = stock_data.replace(' ', '')
        stock_list = stock_data.split(';')[:-1]
        stock_list = [stock.split(',') for stock in stock_list]
        for stock in stock_list:
            stock[1] = int(stock[1])
            stock[2] = float(stock[2])
        df = pd.DataFrame(stock_list, columns=columns)
        return df
