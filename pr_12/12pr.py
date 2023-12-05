import requests
from pprint import pprint
from tkinter import *


def find():
     username =okno1.get()
     url = f"https://api.github.com/users/{username}"
     user_data = requests.get(url).json()
     pprint(user_data)

window=Tk()
window.title('Чижов Никита Андреевич')
okno1= Entry(window,width=6)
okno1.grid(column=0, row=0)
lbl=Button(window, text="find",command=find,width=10)
lbl.grid(column=4, row=0)
window.mainloop()
