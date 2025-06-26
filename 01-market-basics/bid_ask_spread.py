import yfinance as yf

def get_bid_ask(ticker):
    stock = yf.Ticker(ticker)
    bid = stock.info['bid']
    ask = stock.info['ask']
    spread = ask - bid
    print(f"{ticker} Bid: ${bid: .2f}, Ask: ${ask: .2f}, Spread: ${spread: .2f}")

if __name__ == "__main__":
    get_bid_ask("TSLA")