
import requests
import bs4

import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_detail():
    url = "https://worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""


    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_detail = all_detail + text + " " + count + "\n"

    return(all_detail)

def get_country_data():
    name=textfeild.get()
    url = "https://worldometers.info/coronavirus/country/" + name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""


    for block in info_div:
        text = block.find("h1", class_=None).get_text()
        count = block.find("span", class_=None).get_text()
        all_detail = all_detail + text + " " + count + "\n"
    
    mainlabel['text']=all_detail    


def reload(): #creating the relaod button
    new_data = get_covid_detail()
    mainlabel["text"] = new_data
    


get_covid_detail()

root = tk.Tk()
root.geometry("900x700")
root.title("Covid19 Tracker")
f = ("poppins", 30, "bold")

banner = tk.PhotoImage(file="covid.png") # to create banner
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

textfeild = tk.Entry(root,width =50)
textfeild.pack()

mainlabel = tk.Label(root, text = get_covid_detail(), font=f)
mainlabel.pack()

gbtn = tk.Button(root, text="Get data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()

root.mainloop()