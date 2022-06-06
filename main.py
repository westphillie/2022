from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.fangraphs.com/prospects/the-board/2022-mlb-draft/summary?sort=-1,1&type=0&pageitems=10000000000000&pg=0'

browser = Browser('chrome')

# open the fangraphs page
browser.visit(url)

# retrieve and parse the html
soup = BeautifulSoup(browser.html, 'lxml')

# find all tables in the html
all_tables = soup.find_all('table')

# converting the last table (the one with the prospects) to str
prospect_table = str(all_tables[-1])

# convert the string containing html to a dataframe
prospects = pd.read_html(prospect_table)

# now we can do anything with the dataframe 
print(prospects)

browser.quit()