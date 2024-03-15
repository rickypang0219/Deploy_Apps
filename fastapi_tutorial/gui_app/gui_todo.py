import tkinter as tk
import customtkinter as ck
import requests


# API URL from localhost
API_URL = "http://127.0.0.1:8000"

# set apperance mode as system
ck.set_appearance_mode("light")

# set window
window = ck.CTk()


# Modify the title, geometry of the window
window.title("Todo App")
window.geometry("600x400")


# define fetch data function
def fetch_data():
    try:
        url = API_URL
        response = requests.get(url)
        data = response.json()
        print(data)
        return data["data"]
    except Exception as e:
        print(e)
        return None


# start the window
fetch_data()
window.mainloop()
