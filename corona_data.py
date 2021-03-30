import tkinter as tk
import requests
import datetime

def get_covid_data():
    api = 'https://disease.sh/v3/covid-19/gov/India'
    json_data = requests.get(api).json()
    total_active = str(json_data['total']["active"])
    total_deaths = str(json_data['total']["deaths"])
    today_cases = str(json_data['total']["todayCases"])
    today_active_cases = str(json_data['total']["todayActive"])
    today_recovered = str(json_data['total']["todayRecovered"])
    today_death = str(json_data['total']["todayDeaths"])
    updated_on = json_data["updated"]
    date = str(datetime.datetime.fromtimestamp(updated_on/1e3))
    label.config(text="Total Active Cases: " + total_active+ "\n" +"Total Deaths: "+total_deaths+"\n"+ "Today Cases: "+ today_cases+"\n"+ "Today Death: "+today_death+ '\n'+"Today Recovered: "+ today_recovered+'\n'+ "Today Active Cases: "+ today_active_cases, fg="red")
    label2.config(text="Data Updated On: "+ date[:11])


canvas = tk.Tk()
canvas.geometry('500x550')
canvas.title("Corona Tracker")

font_style = ('Helvetica', 10, 'bold')
button = tk.Button(canvas, font=font_style, text='Refresh', command=get_covid_data, bg ='yellow')
button.pack(pady=20)

head = tk.Label(canvas, text="Corona Data of India", justify='left', font='Helvetica 11 bold')
head.pack(pady=5)
label = tk.Label(canvas, font=font_style, justify='left')
label.pack(pady=20)

label2 = tk.Label(canvas, font=font_style, justify='left')
label2.pack()
get_covid_data()

canvas.mainloop()


# # api = 'https://disease.sh/v3/covid-19/gov/India'
# # json_data = requests.get(api).json()
# # print(json_data['total']['active'])