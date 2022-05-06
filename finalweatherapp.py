import requests
from tkinter import *


def weatherreport(str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={str}&appid=ce0e0fcb658e76c6146aca93a6602d5e"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    x = response.json()
    ab = x['main']
    temp = ab['temp']
    indegree= "{:.2f}".format(temp-273)
    feel = ab['feels_like']
    indegree2 = "{:.2f}".format(feel - 273)
    matemp = ab['temp_max']
    indegree3= "{:.2f}".format(matemp-273)
    mitemp = ab['temp_min']
    indegree4 = "{:.2f}".format(mitemp - 273)
    hum = ab['humidity']
    pr = ab['pressure']
    return (indegree, indegree2, indegree3, indegree4, hum, pr)


def takecity():
    string = City.get()
    return string

def delete_city():
    City.delete("0","end")


def sendcity(func):
    argue = func()
    text = weatherreport(argue)
    City_name.insert(END, argue)
    Temprature.insert(0, text[0])
    Feelslike.insert(0, text[1])
    max_temp.insert(0, text[2])
    min_temp.insert(0, text[3])
    Humidity.insert(0, text[4])
    Pressure.insert(0, text[5])
    
def delete_all_text():
    City_name.delete("0","end")
    Temprature.delete("0","end")
    Feelslike.delete("0","end")
    max_temp.delete("0","end")
    min_temp.delete("0","end")
    Humidity.delete("0","end")
    Pressure.delete("0","end")



window = Tk()
window.title("weather update")
window.geometry("300x200")
Label(window, text="Enter City", bg="sky blue").grid(row=0)
Label(window, text="City Name", bg="sky blue").grid(row=1)
Label(window, text="Temprature", bg="sky blue").grid(row=2)
Label(window, text="Feels like", bg="sky blue").grid(row=3)
Label(window, text="Max. temprature", bg="sky blue").grid(row=4)
Label(window, text="Min. temprature", bg="sky blue").grid(row=5)
Label(window, text="Humidity", bg="sky blue").grid(row=6)
Label(window, text="Pressure", bg="sky blue").grid(row=7)
button = Button(window, text="Enter",bg="MistyRose", width=10, command=lambda: [delete_all_text(),sendcity(takecity), delete_city()])
button.grid(row=9, column=1)
City = Entry(window)
City_name= Entry(window)
Temprature = Entry(window)
Feelslike = Entry(window)
max_temp = Entry(window)
min_temp = Entry(window)
Humidity = Entry(window)
Pressure = Entry(window)
City.grid(row=0, column=1)
City_name.grid(row=1, column=1)
Temprature.grid(row=2, column=1)
Feelslike.grid(row=3, column=1)
max_temp.grid(row=4, column=1)
min_temp.grid(row=5, column=1)
Humidity.grid(row=6, column=1)
Pressure.grid(row=7, column=1)

window.configure(bg='sky blue')
mainloop()
