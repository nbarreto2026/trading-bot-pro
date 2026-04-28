import pandas_ta as ta

def apply_indicators(df):
    df['EMA_9'] = ta.ema(df['Close'], length=9)
    df['EMA_26'] = ta.ema(df['Close'], length=26)
    df['EMA_50'] = ta.ema(df['Close'], length=50)
    df['RSI'] = ta.rsi(df['Close'], length=14)

    return df
