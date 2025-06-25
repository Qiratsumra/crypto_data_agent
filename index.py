import requests
import chainlit as cl

from dotenv import load_dotenv

load_dotenv()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Welcome to the Crypto Price Tracker! You can ask me about the current prices of cryptocurrencies.\n Top 10 to get the top 10 cryptocurrencies by price."
    ).send()

@cl.on_message
async def handle_message(message:cl.Message):
    user_input = message.content.strip().upper()
    if user_input == "Top 10":
        url = "https://api.binance.com/api/v3/ticker/price"
        try:
            response =  requests.get(url)
            data = response.json()
            top_10 = "\n".join([f"{coin["symbol"]}: {coin["price"]}USDT" for coin in data[:10]])
            await cl.Message(f"Top 10 cryptocurrencies by price:\n{top_10}").send()
        except Exception as e:
            await cl.Message("Error fetching data from Binance API: " + str(e)).send()
    else:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={user_input}USDT"
        try:
            response =requests.get(url)
            if response.status_code == 200:
                data = response.json()
                await cl.Message(f"The current price of {user_input} is {data['price']} USDT.").send()
            else:
                await cl.Message(f"Could not find data for {user_input}. Please check the symbol and try again.").send()
        except Exception as e:
            await cl.Message("Error fetching data from Binance API: " + str(e)).send()
        