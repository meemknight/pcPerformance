import requests
from pprint import pprint
from bs4 import BeautifulSoup
from pcData import *

def medieLuna(date):
    r = requests.get('https://www.top500.org/lists/top500/' + date)
    
    if not r.ok:
        return None

    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find('table', class_="table table-condensed table-striped")
    tableRow = table.find_all('tr') 

    tableHeader = soup.find('thead')
    tableHeaderRow = tableHeader.find('tr').find_all('th')
    tableMeasurement = tableHeaderRow[3].text
    
    divisor = 1
    if 'GFlop/s' in tableMeasurement:
        divisor = 1000


    count = 0
    medie = PcData()
    
    for i in tableRow:

        tableData = i.find_all('td')
        


        if len(tableData) > 2:

            medie.cores +=  int(tableData[2].text.replace(',',""))
            medie.rmax +=   float(tableData[3].text.replace(',',"")) / divisor
            medie.rpeak +=  float(tableData[4].text.replace(',',"")) / divisor
            #medie.power +=  float(tableData[5].text.replace(',',""))
            #print(tableData[2].text)
            count += 1
            if count >= 3:
                break
    
    medie.divide(count)

    return medie

def medieAn(date):

    medie = PcData()
    count = 0

    for i in [6, 11]:
        luna = medieLuna(date + "/" + str(i))
        if luna:
            medie.add(luna)
            count += 1
        
    medie.divide(count)
    return medie

#medie = medieAn("2019")
#print("cpre  count: ", medie.cores)
#print("rmax  count: ", medie.rmax)
#print("rpeak count: ", medie.rpeak)
#print("power count: ", medie.power)

medii = []
ani = [i for i in range(1993, 2021)]

for i in ani:
    medii.append(medieAn(str(i)))
    print(f"medie anul {i} done")

index = 0

print("rmax values(tflops/s):")
year = ani[0]

rmaxMedie = 0

while index < len(medii) - 1:

    print(f"anul: {ani[index]}-{ani[index+1]} progres: {medii[index+1].rmax - medii[index].rmax}")
    rmaxMedie = medii[index+1].rmax - medii[index].rmax
    index += 1

#print("cpre  count: ", medie.cores)
#print("rmax  count: ", medie.rmax)
#print("rpeak count: ", medie.rpeak)
#print("power count: ", medie.power)

print(f"Medie = {rmaxMedie / index}")