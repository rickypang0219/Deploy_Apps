import requests


API_KEY = "fca_live_HKfRmogF19gnJ3U32xRKr766urt1EJOznatidvAE"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD"]


def convert(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&currencies={currencies}&base_currency={base}"
    try:
        response = requests.get(url)
        data = response.json()
        # print(data)
        return data["data"]
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    while True:
        # ask what is the base of the currency
        base = input("What is the base of the currency? (eg: HKD in capital form) ; q for quiting: ")
        base = base.upper()
        
        # check if quitting 
        if base == 'Q':
            break 

        # ask what is the dollar
        cash = input("How much curreny do you have?")

        data = convert(base)
        for ticker, value in data.items():
            print(f"{ticker}:{ float(cash) * value}")
