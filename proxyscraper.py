import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = [] # create list to contain scraped data

def deletelist():
    list_of_rows.clear() # used to delete scraped proxies when each different site is selected

def saveproxy(): # function to ask user to input name of file containing the scraped proxies 
    filename = input("Please input name of file to be saved")        
    with open (filename + '.csv','w') as file:
        writer=csv.writer(file)
        writer.writerow(['IP Address','Port', 'Code', 'Country', 'Anonymity', 'Google', 'HTTPS', 'Last Checked'])
        for row in list_of_rows:
            writer.writerow(row)
    print("File Saved Successfully")

def makesoup(url): # pass url to beautifulsoup to parse html. Url is defined in menu for each site so code doesnt have to be repeated for each site
    page=requests.get(url)
    print(url + "  scraped successfully")
    return BeautifulSoup(page.text,"lxml")

def proxyscrape(table): # scrape proxy data from table on site, add to list that was created earlier
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

def scrapeproxies(url): # contains the parent  table attribute where proxy data is present 
    soup=makesoup(url)
    proxyscrape(table = soup.find('table', attrs={'id': 'proxylisttable'}))

def menu(): # menu displayed to user to select option
        strs = ('Enter 1 to Scrape Proxies from http://sslproxies.org\n'
                'Enter 2 to Scrape Proxies from http://free-proxy-list.net\n'
                'Enter 3 to Scrape Proxies from http://us-proxy.org\n'
                'Enter 4 to Scrape Proxies from http://socks-proxy.net\n'
                'Enter 5 to Exit\n' )
        choice = input(strs)
        return int(choice) 

while True:          #use while True
    choice = menu()
    if choice == 1:
        scrapeproxies(url = "https://www.sslproxies.org")
    elif choice == 2:
        scrapeproxies(url = "https://free-proxy-list.net")
    elif choice == 3:
        scrapeproxies(url = "https://us-proxy.org")
    elif choice == 4:
        scrapeproxies(url = "https://socks-proxy.net")
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
    if 1 <= choice <= 4:
        saveproxy()
        deletelist() # this deletes proxies from list to ensure no proxies remain in list after file is created. This ensures list is empty and ready for proxies from selected site to be scraped. 

    
