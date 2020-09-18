import yfinance as yf
import os

# Quick demo project to test out Actions
class slackChecker():

    def __init__(self, symbol):
        self.symbol = symbol

    def get_latest_info(self):
        tickerSymbol = self.symbol
        tickerData = yf.Ticker(tickerSymbol)
        print(tickerData.recommendations)
        print(tickerData.info)
        return tickerData.info


def main():
    # Read the stock name set in the env variable in the workflow
    sc = slackChecker(os.environ['STOCK_NAME'])
    sc.get_latest_info()


if __name__ == '__main__':
    main()
