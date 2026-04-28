import yfinance as yf

def get_data(ticker):
    try:
        df = yf.download(ticker, period="150d", interval="1d", progress=False)
        return df
    except Exception as e:
        print(f"Error descargando {ticker}: {e}")
        return None
