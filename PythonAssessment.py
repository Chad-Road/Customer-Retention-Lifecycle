from bs4 import BeautifulSoup
import requests
import numpy as np

census_page_raw = requests.get('https://www.census.gov/programs-surveys/popest.html')
census_page_content = census_page_raw.content
scrape = BeautifulSoup(census_page_content, 'html.parser')

census_links_raw = []
census_links = []

for link in scrape.find_all('a'):
    census_links_raw.append(link.get('href'))

# removes all values that don't start with either 'h' or '/'
for raw in census_links_raw:
    if raw:
        if raw[0] == 'h':
            census_links.append(raw.rstrip('/'))
        elif raw[0] == '/':
            census_links.append('https://www.census.gov' + raw.rstrip('/'))

# converts list to dictionary keys then back into list to remove possible duplicates           
census_links = list(dict.fromkeys(census_links))

np.savetxt('census_csv.csv', census_links, delimiter=',', fmt='%s')

print('Successfully completed scrape and saved results to csv')


  


