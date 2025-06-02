import tkinter as tk
from tkinter import scrolledtext

# Expanded Crypto Database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3.0,
        "volatility": "high"
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6.0,
        "volatility": "medium"
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8.0,
        "volatility": "medium"
    },
    "Polkadot": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9.0,
        "volatility": "medium"
    },
    "Algorand": {
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "very low",
        "sustainability_score": 9.5,
        "volatility": "low"
    },
    "Solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7.0,
        "volatility": "high"
    }
}

# Chatbot Logic
def crypto_buddy(user_query):
    user_query = user_query.lower()

    if "eco-friendly" in user_query or "most sustainable" in user_query:
        eco_coins = sorted(
            [coin for coin in crypto_db if crypto_db[coin]["sustainability_score"] >= 8],
            key=lambda x: -crypto_db[x]["sustainability_score"]
        )
        reply = "Most Sustainable Coins 🌿:\n"
        for coin in eco_coins:
            reply += f"{coin}: Sustainability {crypto_db[coin]['sustainability_score']}/10, Energy: {crypto_db[coin]['energy_use'].capitalize()}\n"
        reply += "These have lower environmental impact!"
        return reply

    elif "compare" in user_query:
        coins = [coin for coin in crypto_db if coin.lower() in user_query]
        if len(coins) == 2:
            a, b = coins
            a_data, b_data = crypto_db[a], crypto_db[b]
            return (
                f"{a} vs {b}:\n"
                f"Price Trend: {a_data['price_trend'].capitalize()} vs {b_data['price_trend'].capitalize()}\n"
                f"Sustainability: {a_data['sustainability_score']}/10 vs {b_data['sustainability_score']}/10\n"
                f"Energy Use: {a_data['energy_use'].capitalize()} vs {b_data['energy_use'].capitalize()}\n"
                f"Volatility: {a_data['volatility'].capitalize()} vs {b_data['volatility'].capitalize()}\n"
                f"Market Cap: {a_data['market_cap'].capitalize()} vs {b_data['market_cap'].capitalize()}"
            )
        else:
            return "Please specify two valid cryptocurrencies to compare."

    elif "long-term" in user_query or "what should i buy" in user_query:
        long_term = [coin for coin in crypto_db if crypto_db[coin]["sustainability_score"] >= 8 and crypto_db[coin]["price_trend"] in ["rising", "stable"]]
        if long_term:
            return (
                "For long-term growth, consider these sustainable coins with solid fundamentals:\n" +
                ", ".join(long_term) +
                "\n\nRemember: ⏳ Long-term means 5+ years! Always diversify your portfolio."
            )
        return "No strong long-term candidates available now."

    elif "risky" in user_query:
        risky = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "high" and crypto_db[coin]["sustainability_score"] < 5]
        return f"Risky investments ⚠️: {', '.join(risky)}" if risky else "No risky coins found."

    elif "list" in user_query:
        return f"All available cryptocurrencies: {', '.join(crypto_db.keys())}"

    elif "help" in user_query:
        return (
            "Available Commands:\n"
            "- What's the most eco-friendly cryptocurrency?\n"
            "- Compare Bitcoin and Solana\n"
            "- What should I buy for long-term?\n"
            "- Show risky investments\n"
            "- Tell me about Cardano\n"
            "- List all cryptocurrencies\n"
            "- Type 'exit' to quit.\n"
            "⚠️ Disclaimer: Cryptocurrency investments are highly volatile and involve substantial risk. This bot is for educational use only!"
        )

    elif "tell me about" in user_query:
        for coin in crypto_db:
            if coin.lower() in user_query:
                data = crypto_db[coin]
                return (
                    f"{coin} Overview:\n"
                    f"- Price Trend: {data['price_trend']}\n"
                    f"- Market Cap: {data['market_cap']}\n"
                    f"- Energy Use: {data['energy_use']}\n"
                    f"- Sustainability Score: {data['sustainability_score']}/10\n"
                    f"- Volatility: {data['volatility']}"
                )
        return "I couldn’t find that cryptocurrency. Try 'list' to see available options."

    else:
        return "I didn't get that 🤖. Type 'help' to see what I can do!"

# GUI Interface with Tkinter
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.insert(tk.END, f"You: {user_input}\n", 'user')
    response = crypto_buddy(user_input)
    chat_log.insert(tk.END, f"CryptoBuddy: {response}\n\n", 'bot')
    entry.delete(0, tk.END)

# Set up GUI window
root = tk.Tk()
root.title("CryptoBuddy Chatbot 💬")

# Chat display
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25, font=("Helvetica", 12))
chat_log.pack(padx=10, pady=10)
chat_log.tag_config('user', foreground='blue')
chat_log.tag_config('bot', foreground='green')

# User entry field
entry = tk.Entry(root, font=("Helvetica", 12), width=60)
entry.pack(padx=10, pady=(0, 10), side=tk.LEFT, expand=True, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=(0, 10), pady=(0, 10), side=tk.RIGHT)

# Start application
root.mainloop()

