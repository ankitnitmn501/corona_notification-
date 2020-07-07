from plyer import notification
from bs4 import BeautifulSoup
import time
import requests

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "corona.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        myHtmlData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData,'html.parser')
        myDataStr =""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text() 
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Uttar Pradesh','Delhi','Maharashtra','Manipur']
        for item in itemList[0:35]:
            datalist = item.split("\n")
            if datalist[1] in states:
                ntitle = 'Status of Covid-19'
                ntext  = f"state : {datalist[1]}\nTotalCases : {datalist[5]}\nActive : {datalist[2]}\nDeath : {datalist[4]}"
                notifyMe(ntitle,ntext)
                time.sleep(3)
        time.sleep(3600)