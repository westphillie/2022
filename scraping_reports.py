from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
from njcaa import * #college_classifications.py

executable_path = {'executable_path':r'/Users/leonardocardozo/PycharmProjects/PhilliesFangraphsDraft/chromedriver'}

url = 'https://www.fangraphs.com/prospects/the-board/2022-mlb-draft/summary?sort=-1,1&type=0&pageitems=10000000000000&pg=0'

browser = Browser('chrome', **executable_path)

browser.visit(url)


soup = BeautifulSoup(browser.html, 'lxml')

all_tables = soup.find_all('table')

prospect_table = str(all_tables[-1])

df = pd.read_html(prospect_table)

number_of_reports = len(df[0].index) + 4

reports_completed = 0
all_reports = []

while number_of_reports > reports_completed:

    is_report = browser.evaluate_script(f"document.getElementsByClassName('material-icons')[{reports_completed}].innerHTML;")

    if is_report == 'assignment':

        browser.execute_script(f"reportBtn = document.getElementsByClassName('material-icons')[{reports_completed}]; reportBtn.click();")

        report = browser.evaluate_script("outerDiv = document.getElementsByClassName('the-board-summary-insert')[0]; innerDiv = outerDiv.getElementsByTagName('div')[0]; spanText = innerDiv.getElementsByTagName('span')[0].innerText; return spanText;")

        all_reports.append(report.text)

    reports_completed += 1

for i in range(len(all_reports)):
    all_reports[i] = all_reports[i][12:]

df[0]['Report'] = all_reports



School_Type = []

for school in df[0]['School']:
    School_Type.append(college_type(school))

df[0]['School Type'] = School_Type

df[0].to_csv('./prospects.csv')

browser.quit()