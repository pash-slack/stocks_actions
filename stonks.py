import yfinance as yf


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
    sc = slackChecker('WORK')
    sc.get_latest_info()


if __name__ == '__main__':
    main()
