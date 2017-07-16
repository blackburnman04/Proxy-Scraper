import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = []

def deletelist():
    list_of_rows.clear()

def saveproxy():
    filename = input("Please input name of file to be saved")        
    with open (filename + '.csv','w') as file:
        writer=csv.writer(file)
        writer.writerow(['IP Address','Port', 'Code', 'Country', 'Anonymity', 'Google', 'HTTPS', 'Last Checked'])
        for row in list_of_rows:
            writer.writerow(row)
    print("File Saved Successfully")

def makesoup(url):
    page=requests.get(url)
    print(url + "  scraped successfully")
    return BeautifulSoup(page.text,"lxml")

def sslproxiesorgscrape(table):
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

def scrapesslproxiesorg():
    soup=makesoup(url = "https://www.sslproxies.org")
    sslproxiesorgscrape(table = soup.find('table', attrs={'id': 'proxylisttable'}))

def menu():
        strs = ('Enter 1 to Scrape Proxies from http://sslproxies.org\n'
                'Enter 2 to Exit\n' )
        choice = input(strs)
        return int(choice) 

while True:          #use while True
    choice = menu()
    if choice == 1:
        scrapesslproxiesorg()
        saveproxy()
        deletelist()
    elif choice == 2:
        break
