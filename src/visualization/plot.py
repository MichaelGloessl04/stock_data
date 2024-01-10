import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_stock_data(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))

    unique_stocks = df['stock'].unique()
    colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_stocks)))

    for stock, color in zip(unique_stocks, colors):
        data = df[df['stock'] == stock]
        plt.plot(data['date'], data['price'], label=stock, color=color)

    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.show()
