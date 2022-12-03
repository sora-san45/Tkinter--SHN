import tkinter as tk
import requests
r=requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=cecf960d')

data = r.json()
