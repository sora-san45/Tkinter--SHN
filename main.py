from tkinter import *
from PIL import Image,ImageTk
import os
import requests
from io import BytesIO

tk=Tk()
tk.geometry("700x500")


tk.title('Movies')  
frame = Frame(tk, width=100, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
def get_movie():
    r=requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=cecf960d')
    data = r.json()
    image1=data["Poster"]
    image1=str(image1)
    response = requests.get(image1)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    return img
    
get_button = Button(tk, text="Get Movie", command=get_movie)
get_button.place(relx=0.5,rely=0.9,anchor=S)
img=get_movie()
label = Label(frame, image=img)
label.pack(side="bottom", fill="both", expand="yes")
tk.mainloop()

