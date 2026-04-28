from app.services.n8n_service import enviar_a_n8n

def dispatch_signal(ticker, signal):
    payload = {
        "ticker": ticker,
        "precio": round(signal["precio"], 2),
        "rsi": round(signal["rsi"], 2),
        "strategy": "swing_pro"
    }

    enviar_a_n8n(payload)

    return payload
