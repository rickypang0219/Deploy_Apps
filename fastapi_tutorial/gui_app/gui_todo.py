import tkinter as tk
from tkinter import ttk
import customtkinter as ck
import requests


# API URL from localhost
API_URL = "http://127.0.0.1:8000/"
N_count = 0

# set apperance mode as system
ck.set_appearance_mode("light")

# set window
window = ck.CTk()


# Modify the title, geometry of the window
window.title("Todo App")
window.geometry("600x400")

# define label
label = ck.CTkLabel(window, text="", font=("Helvetica", 24))
label.pack(pady=10)


# enter the content of a todo
content = ck.CTkEntry(window, placeholder_text="Enter content", width=200, height=50)
content.pack(pady=10)


# define PUT method
def put_data(content):
    global N_count
    url = API_URL + "items"
    data = {"id": N_count, "content": content.get(), "finished": False}
    N_count += 1
    requests.post(url, json=data)


# fetch and display data
def fetch_display_data():
    try:
        url = API_URL
        response = requests.get(url)
        response = response.json()

        # clear previous item
        listbox.delete(0, tk.END)

        for item in response:
            listbox.insert(tk.END, item)
    except Exception as e:
        print(e)
        return []


def post_data(content):
    global N_count
    url = API_URL + "items"
    data = {"id": N_count, "content": content.get(), "finished": False}
    N_count += 1
    requests.post(url, json=data)
    fetch_display_data()


def sumbit(content):
    post_data(content)


submit_button = ck.CTkButton(window, text="submit", command=lambda: sumbit(content))
submit_button.pack(pady=10)

listbox = tk.Listbox(window, width=50)
listbox.pack()


# Create a Listbox with a custom style
listbox = tk.Listbox(window, width=50)
listbox.pack()

# start the window
window.mainloop()
