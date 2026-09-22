import requests
from bs4 import BeautifulSoup

def get_etf_data(symbol):
    url = f"https://www.bankier.pl/inwestowanie/profile/quote.html?symbol={symbol}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get the percentage change and date elements
        var_percentage_change = soup.find('span', class_='-percentage-change')
        var_date = soup.find('span', class_='-date')

        if var_percentage_change and var_date:
            return (symbol, var_percentage_change.text.strip(), var_date.text.strip())

        return "Missing data"

    except Exception as e:
        return f"Error: {e}"

# --- Test ---
etfs = ["ETFPZUWORLD","ETFPZUW20M40","ETFPZUGOLD"]
for etf in etfs:
    result = get_etf_data(etf)
    print(result)