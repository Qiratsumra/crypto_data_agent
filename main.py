import requests
import streamlit as st

st.set_page_config(page_title="Crypto Tracker", page_icon=":money_with_wings:", layout="wide")
st.title("Crypto Tracker :money_with_wings:")


def show_top_coins():
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response =  requests.get(url)
        response.raise_for_status() #Raise HTTPError for bad responses, if occurs
        data = response.json()

        st.subheader("Top 10 cryptocurrencies by price:")
        for coin in data[:10]:  # Get the first 10 coins
            st.success(f"{coin['symbol']}: ${coin['price']} USDT")

    except requests.exceptions.RequestException as e:
        st.error("Error fetching data from Binance API:", e)


def show_specific_coin(coin_symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin_symbol.upper()}USDT"
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            st.info(f"Current price of {coin_symbol.upper()}: ${data['price']} USDT")
        else:
            st.error(f"Error fetching data for {coin_symbol.upper()} not found in Binance.")   
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data for {coin_symbol.upper()}: {e}") 

def main():
    st.sidebar.title("Navigation")
    options = ["Top Coins", "Specific Coin"]
    choice = st.sidebar.selectbox("Select an option", options)

    if choice == "Top Coins":
        show_top_coins()
    elif choice == "Specific Coin":
        coin_symbol = st.sidebar.text_input("Enter coin symbol (e.g., BTC, ETH):")
        if coin_symbol:
            show_specific_coin(coin_symbol)


if __name__ == "__main__":
    main()

















# import os
# import streamlit as st
# import requests
# from dotenv import load_dotenv


# # ---- Load Environment Variables ----
# load_dotenv()

# # ---- Gemini API Config ----
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# BASE_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

# # ---- Function to Fetch Coin Data from CoinLore ----
# def get_coin_data(coin_name):
#     try:
#         url = "https://api.coinlore.net/api/tickers/"
#         response = requests.get(url)
#         data = response.json().get("data", [])

#         for coin in data:
#             if coin_name.lower() in coin["name"].lower() or coin_name.lower() == coin["symbol"].lower():
#                 price = coin["price_usd"]
#                 rank = coin["rank"]
#                 return price, rank

#         return "0", "Coin not found in CoinLore database."

#     except Exception as e:
#         return "Error", str(e)

# # ---- Function to Query Gemini LLM ----
# def ask_gemini(prompt):
#     headers = {"Content-Type": "application/json"}
#     params = {"key": GEMINI_API_KEY}
#     body = {
#             "contents": [{"parts": [{"text": prompt}]}]
#         }

#     response = requests.post(BASE_URL, params=params, headers=headers, json=body)
#     result = response.json()
#     return result


# # ---- Streamlit Frontend ----


# st.set_page_config(page_title="CryptoData Price Agent (Gemini)", page_icon="💹")

# st.title("💹💵 CryptoData Price Agent Created by Qirat Saeed")


# coin_name = st.text_input("Enter Coin Name(e.g., Bitcoin or BTC):")

# if st.button("Get Price & Rank"):
#     if coin_name:
#         with st.spinner("Fetching Data..."):
#             price, rank = get_coin_data(coin_name)
#             ai_prompt = (
#                 f"User asked for {coin_name} price and market rank.\n"
#                 f"Current Price: {price} USD\n"
#                 f"Market Rank: {rank}\n"
#                 "Explain this data to a beginner-friendly audience."
#             )
#             ai_response = ask_gemini(ai_prompt)

#         st.success(f"💰 Price: {price} USD")
#         st.info(f"🏅 Market Rank: {rank}")
       
           
#     else:
#         st.warning("Please enter a valid coin name or symbol.")

# st.caption("**Created by Qirat Saeed**")