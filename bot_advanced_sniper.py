import telebot
from flask import Flask, request
import threading

BOT_TOKEN = "8105740927:AAE_6CvRG9rbBdTGLuQGQ3t-SbvhIW-uUnk"
CHAT_ID = 7407138270  # Replace with your actual Telegram ID

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print("📩 Received:", data)

        # Core Data
        symbol = data.get("symbol", "BTC/USDT")
        signal = data.get("signal", "BUY").upper()
        rsi = data.get("rsi", "N/A")
        macd = data.get("macd", "N/A")
        entry = data.get("entry", "N/A")
        tp = data.get("tp", "N/A")
        sl = data.get("sl", "N/A")

        # Pro-Level Add-ons
        confidence = data.get("confidence", "High")
        volume_spike = data.get("volume_spike", "✅")
        oi_change = data.get("oi_change", "N/A")
        support = data.get("support", "N/A")
        resistance = data.get("resistance", "N/A")
        sentiment = data.get("sentiment", "Neutral")
        funding = data.get("funding_rate", "N/A")
        whale_alert = data.get("whale_alert", "None")
        screenshot_url = data.get("screenshot_url", None)

        # Build Message
        message = (
            f"🚨 *SNIPER TRADE ALERT*\n\n"
            f"🪙 *Symbol:* {symbol}\n"
            f"💹 *Signal:* {signal} (RSI + MACD Confirmed)\n"
            f"📊 *RSI:* {rsi} | *MACD:* {macd}\n"
            f"📦 *Volume Spike:* {volume_spike} | *OI Change:* {oi_change}\n"
            f"🔹 *Support:* {support} | 🔺 *Resistance:* {resistance}\n"
            f"🐋 *Whale:* {whale_alert}\n"
            f"📈 *Sentiment:* {sentiment} | *Funding:* {funding}\n\n"
            f"🎯 *Entry:* {entry}\n"
            f"✅ *TP:* {tp} | ❌ *SL:* {sl}\n"
            f"🧠 *Confidence:* {confidence}"
        )

        bot.send_message(CHAT_ID, message, parse_mode="Markdown")

        # Send Screenshot (if included)
        if screenshot_url:
            bot.send_photo(CHAT_ID, screenshot_url)

        return "OK", 200

    except Exception as e:
        print("❌ ERROR:", e)
        return "ERROR", 500

def run_flask():
    app.run(host="0.0.0.0", port=5000)

threading.Thread(target=run_flask).start()
print("🚀 Sniper Pro Bot is LIVE and waiting for TradingView alerts...")
while True:
    pass
