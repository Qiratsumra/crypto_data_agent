# import requests
# import json

# def get_crypto_data(api_url):
#   """
#   Fetches cryptocurrency data from the given API URL.

#   Args:
#     api_url: The URL of the API endpoint.

#   Returns:
#     A dictionary containing the API response as a JSON object, or None if there was an error.
#   """
#   try:
#     response = requests.get(api_url)
#     response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
#     return response.json()
#   except requests.exceptions.RequestException as e:
#     print(f"Error fetching data from API: {e}")
#     return None

# def analyze_crypto_trends(data, coin_symbols):
#   """
#   Analyzes the cryptocurrency data and prints the current price and a brief trend analysis for specified coins.       

#   Args:
#     data: A dictionary containing the cryptocurrency data.
#     coin_symbols: A list of cryptocurrency symbols to analyze (e.g., ["BTC", "ETH"]).
#   """
#   if not data or "data" not in data:
#     print("Invalid data format.  Expected a dictionary with a 'data' key.")
#     return

#   coins_data = data["data"]
#   for symbol in coin_symbols:
#     coin = next((c for c in coins_data if c["symbol"] == symbol), None)
#     if coin:
#       price_usd = coin["price_usd"]
#       change_24h = coin["percent_change_24h"]
#       print(f"Current price of {symbol}: ${price_usd}")
#       if float(change_24h) >= 0:
#         print(f"In the last 24 hours, {symbol} has increased by {change_24h}%.")
#       else:
#         print(f"In the last 24 hours, {symbol} has decreased by {change_24h}%.")
#     else:
#       print(f"Could not find data for {symbol}")

# # Main execution
# api_url = "https://api.coinlore.net/api/tickers/"
# crypto_data = get_crypto_data(api_url)

# if crypto_data:
#   analyze_crypto_trends(crypto_data, ["BTC", "ETH"])















import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
provider = AsyncOpenAI(
    api_key= api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    openai_client= provider,
    model='gemini-2.0-flash'
)

agent = Agent(
    name= "Crypto Data Agent",
    instructions= "You are a crypto data agent that give the coin price and listed date! not give data in json formate",
    model=model,
)

crypto_api = "https://api.coinlore.net/api/tickers/"
prompt = f"What is the current price of Bitcoin and Ethereum? Provide a brief analysis of their trends from this api: {crypto_api}"
result = Runner.run_sync(agent, prompt)
print(result.final_output)