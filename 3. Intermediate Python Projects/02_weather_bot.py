import requests
import json
import pyttsx3

city = input("Enter your city :\n")
url = f"https://api.weatherapi.com/v1/current.json?key=979f854975d641df869111846252906&q={city}"

engine = pyttsx3.init()
r = requests.get(url)
w_dic = json.loads(r.text)
temp = str(w_dic["current"]["temp_c"])
cloudiness = str(w_dic["current"]['cloud'])
timedate = str(w_dic["location"]["localtime"])
print(f"Temperature : {temp}")
print(f"Cloudiness : {cloudiness}")
print(f"Date & TIme : {timedate}")
temp_speak = "The Temperature of "+city+"is"+ temp
engine.say(temp_speak)
engine.runAndWait()
