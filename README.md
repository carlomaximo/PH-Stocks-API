# PH Stocks API v.1

## What is this?
A simple RESTful API that, given a ticker, returns the ticker and its last traded price in a JSON format. Made in **Python** using **Flask** and **BeautifulSoup**. This API is for **personal use only**.

## Why
idk seems handy
(but fr though, i'm planning to make a stock portfolio app and it does seem useful to have the latest trade prices on hand)
(also, i feel like data should be easily accessible and not gated by a paywall **ehem which is what the PSE does ehem**)

## How to use it?
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create your own .env file with the following variable and format:
    ```env
    CMPY_IDS= {"DMCI": "188","AREIT": "679", "<ticker>": "<id>", ...}
    ```
    - You can get the IDs by inspecting the [PSE company website](https://edge.pse.com.ph/companyDirectory/form.do). The IDs are the numbers in the URL when you click on a stock.
4. Run the Flask app using `python app.py`.
5. JSON is returned at `http://127.0.0.1:5000/<ticker>` in the format:
```json
{
    "ticker": "<ticker>",
    "last_traded_price": "<price>"
}
```
## Sample Usage
```bash
curl http://127.0.0.1:5000/AREIT
```
OR you could use Postman or your handy dandy browser

## Sample Output
```json
{
    "ticker": "AREIT",
    "last_traded_price": "40.00"
}
```

## Disclaimers
- Again, this is for your **personal use only**. I keep seeing on Reddit that it's against PSE's ToS to scrape their website lol (never actually read their ToS in depth, what I saw though was that access is limited for personal, non-commercial use).
- I made the .env workaround ~to make you work for it~ to enforce the 'for your personal use only' thing. If you're lazy though, you can just PM me and I'll send you my file. As of 8 June, I have about ten tickers out of 280+ companies. Not much, but it's something
- My liberal use of AREIT in my examples is not financial advice to buy AREIT lol