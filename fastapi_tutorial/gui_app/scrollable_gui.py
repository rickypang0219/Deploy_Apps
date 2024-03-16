import customtkinter as ck
from PIL import Image
import os
import requests

# Srollable Frame Class
class ScrollableButtonFrame(ck.CTkScrollableFrame):
    def __init__(self, master, command= None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.command = command
        self.radiobutton = ck.StringVar()
        self.label_list = [ ]
        self.button_list = [ ]


    def add_item(self,item, image=None):
        label = ck.CTkLabel(self, text=item, image = image , compound="left", padx=5, anchor="w")
        button = ck.CTkButton(self, text="Command" , width=100, height=24)
        if self.command is not None:
                button.configure(command = lambda: self.command(item))
        label.grid(row = len(self.label_list), column=0, pady=(0,10), padx=5)
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def clear_items(self):
        for label in self.label_list:
            label.destroy()
        for button in self.button_list:
            button.destroy()
        self.label_list.clear()
        self.button_list.clear()


# define post method
def fetch_display_data():
    try:
        url = "http://127.0.0.1:8000"
        response = requests.get(url)
        response = response.json()
        return response
    except Exception as e:
        print(e)
        return []

def post_data(message):
    url = "http://127.0.0.1:8000/items"
    data = {"id": 0, "content": message.get(), "finished": False}
    requests.post(url, json=data)
    fetch_display_data()


def submit(content):
    post_data(content)





# define App class
class App(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("Todo List")
        self.grid_rowconfigure(0 ,weight=1)
        self.columnconfigure(2, weight=1)


        # Add an entry box to enter message
        self.entry = ck.CTkEntry(self, placeholder_text="Content")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(10, 0), pady=(5, 5), sticky="nsew")


        self.submit_button = ck.CTkButton(self, text="submit", command= self.submit_button_clicked)
        self.submit_button.grid(row=3, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")


        # self.data = fetch_display_data()

        # create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableButtonFrame(master=self, width=300, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")

        # for obj in self.data:
        #     self.scrollable_label_button_frame.add_item(f"{obj['content']}",image=ck.CTkImage(Image.open(os.path.join(current_dir, "test_images","chat_light.png"))))
        #

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")

    def submit_button_clicked(self):
        post_data(self.entry)
        self.data = fetch_display_data()
        self.scrollable_label_button_frame.clear_items()

        for obj in self.data:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.scrollable_label_button_frame.add_item(f"{obj['content']}", image=ck.CTkImage(Image.open(os.path.join(current_dir, "test_images", "chat_light.png"))))


if __name__ == "__main__":
    ck.set_appearance_mode("dark")
    app = App()
    app.mainloop()
