import requests
from bs4 import BeautifulSoup
import numpy as np
import textwrap
food = requests.get("https://groot.nmhschool.org/dining/weeklymenu.html")
html = BeautifulSoup(food.text, "html.parser")
menu = np.empty((99, 4), dtype="<U999") #store menu data using np array

# takes <b> elements and ignores any that don't have 0 (i.e not a day/date)
for index in range(len(html.find_all("b"))):
    if "," in html.find_all("b")[index].get_text():
        menu[index-3, 0] = html.find_all("b")[index].get_text().strip("'")

# <br> being stubborn so used this mess to pull strings instead 
def outputlist():
    global menu
    for day in range(99):
        for meal in range(1,4):
            if html.select_one("#GridView1_Label%1d_%1d" % (meal, day)) is None: break
            items = map(str.strip, html.select_one("#GridView1_Label%1d_%1d" % \
                                                   (meal, day)).find_all(string=True))
            menu[day,meal] = ("\n".join(items))
        if html.select_one("#GridView1_Label%1d_%1d" % (meal, day)) is None: break
    for index in range(day):
        print(menu[index, 0] + ":")
        print("   Breakfast/Brunch:\n" + textwrap.indent(menu[index, 1], "      ") \
              + "\n   Lunch:\n" + textwrap.indent(menu[index, 2], "      ") \
              + "\n   Dinner:\n" + textwrap.indent(menu[index, 3], "      ") + "\n")

def outputlines():
    global menu
    for day in range(99):
        for meal in range(1,4):
            if html.select_one("#GridView1_Label%1d_%1d" % (meal, day)) is None: break
            items = map(str.strip, html.select_one("#GridView1_Label%1d_%1d" % \
                                                   (meal, day)).find_all(string=True))
            menu[day,meal] = (", ".join(items))
        if html.select_one("#GridView1_Label%1d_%1d" % (meal, day)) is None: break
    for index in range(day):
        print(menu[index, 0] + ":")
        print("   Breakfast/Brunch:\n" + textwrap.indent(menu[index, 1], "      ") \
              + "\n   Lunch:\n" + textwrap.indent(menu[index, 2], "      ") \
              + "\n   Dinner:\n" + textwrap.indent(menu[index, 3], "      ") + "\n")
