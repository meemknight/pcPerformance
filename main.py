import requests
from pprint import pprint
from bs4 import BeautifulSoup
from pcData import *

def extragereLuna(date):
    r = requests.get('https://www.top500.org/lists/top500/' + date)
    
    if not r.ok:
        return None

    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find('table', class_="table table-condensed table-striped")

    tableRow = table.find_all('tr') 

    count = 0
    medie = PcData()
    
    for i in tableRow:

        tableData = i.find_all('td')

        if len(tableData) > 2:
            medie.cores +=  int(tableData[2].text.replace(',',""))
            medie.rmax +=   float(tableData[3].text.replace(',',""))
            medie.rpeak +=  float(tableData[4].text.replace(',',""))
            medie.power +=  float(tableData[5].text.replace(',',""))
            #print(tableData[2].text)
            count += 1
            if count >= 3:
                break
    
    medie.divide(count)

    return medie

print("cpre count: ", extragereLuna("2020/11").cores)
