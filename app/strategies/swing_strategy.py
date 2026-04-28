def generate_signal(df):
    try:
        ultimo = df.iloc[-1]

        precio = float(ultimo['Close'])
        ema9 = float(ultimo['EMA_9'])
        ema26 = float(ultimo['EMA_26'])
        ema50 = float(ultimo['EMA_50'])
        rsi = float(ultimo['RSI'])

        if precio > ema50 and ema9 > ema26 and rsi < 65:
            return {
                "precio": precio,
                "rsi": rsi
            }

        return None

    except Exception as e:
        print("Error generando señal:", e)
        return None
