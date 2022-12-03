from tkinter import *
from PIL import Image,ImageTk
import requests
from urllib.request import urlopen

tk=Tk()
tk.title('Movies')  
def get_movie():
    r=requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=cecf960d')
    data = r.json()
    image1=data["Poster"]
    print(image1)
    u=urlopen(image1)
    raw_data=u.read()
    u.close()
    img=ImageTk.PhotoImage(data=raw_data)
    label=Label(tk,image=img)
text_box = Text(tk, height=10, width=50)
get_button = Button(tk, text="Get Movie", command=get_movie)
  
text_box.pack()
get_button.pack()
tk.mainloop()

