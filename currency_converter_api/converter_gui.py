import tkinter as tk
import customtkinter as ck
import requests  # for feteching API


# set API for currency converter
API_KEY = "fca_live_HKfRmogF19gnJ3U32xRKr766urt1EJOznatidvAE"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


# set apperance mode as system
ck.set_appearance_mode("light")

# create a window uisng tkinter
window = ck.CTk()

# Modify the title, geometry of the window
window.title("currency_converter")
window.geometry("600x400")

# enter how much cash
capital = ck.CTkEntry(
    window, placeholder_text="Enter how much cash", width=200, height=50
)
capital.pack(pady=10)

base = ck.CTkEntry(window, placeholder_text="Base of currency", width=200, height=50)
base.pack(pady=40)

target = ck.CTkEntry(
    window,
    placeholder_text="Desired currecy (e.g. USA, HKD, AUD, CAD)",
    width=200,
    height=50,
)
target.pack(pady=10)


label = ck.CTkLabel(window, text="", font=("Helvetica", 24))
label.pack(pady=10)


# define convert function
def convert(base, targte):
    # CURRENCIES = ["USD"]
    # currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&currencies={(target.get()).upper()}&base_currency={(base.get()).upper()}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None


# define submit button
def submit(base, target):
    data = convert(base, target)
    for ticker, value in data.items():
        label.configure(
            text=f"you convert {capital.get()} in {base.get()} to { round(value * float(capital.get()), 2) } in  {ticker} "
        )
    # label.configure(text=f"you have {value * float(capital.get())} ")


submit_button = ck.CTkButton(
    window, text="Convert", command=lambda: submit(base, target)
)
submit_button.pack(pady=10)


# start the window
window.mainloop()
