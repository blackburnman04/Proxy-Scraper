# Proxy Scraper 
Proxy Scraper in Python 3 Using Beautiful Soup 4

This script will allow a user to scrape proxies from four different websites:

1. SSLProxies.org <br>
2. Free-Proxy-List.net <br>
3. US-Proxy.org <br>
4. Socks-Proxy.net <br>

Users are able to choose which site they would like to scrape proxies from, from the menu prompted with when first running the script. 

When proxies have been scraped from the site chosen, the user will be prompted to enter the filename of the file to be created to contain the scraped proxy data.

The script creates a .csv file containing the proxy data. 

<b>Dependencies:</b>

-csv <br>
- requests <br>
- beautifulsoup4


<b>Possible future features: </b>

- Implementing a GUI which will show proxies directly in GUI and allow them to be saved to file<br>
- Feature to test proxies that has been scraped to ensure they are live <br>
- Add more sites to scrape from. 
