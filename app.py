import os
import json
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
CMPY_IDS = json.loads(os.getenv("CMPY_IDS"))
app = Flask(__name__)
app.json.sort_keys = False # from https://stackoverflow.com/questions/54446080/how-to-keep-order-of-sorted-dictionary-passed-to-jsonify-function, price going first over ticker was driving me crazy

@app.route('/<ticker>')
def get_price(ticker):
    # replace ticker w/ company ID
    if ticker.upper() not in CMPY_IDS:
        return jsonify({'error': 'Ticker not found'}), 404
    cmpy_id = CMPY_IDS[ticker.upper()]
    print(f"Ticker: {ticker.upper()}, Company ID: {cmpy_id}")

    # insert ID to url
    url = f"https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id={cmpy_id}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # get last traded price
    last_traded_price = None
    for th in soup.find_all("th"):
        if "Last Traded Price" in th.text:
            td = th.find_next_sibling("td")
            if td:
                last_traded_price = float(td.text.strip())
            break

    # return stuff
    if last_traded_price is None:
        return jsonify({'error': 'Price not found'}), 404

    return jsonify({
        'ticker': ticker.upper(),
        'last_traded_price': last_traded_price
    })

# woah holy cow it runs???
if __name__ == '__main__':
    app.run()