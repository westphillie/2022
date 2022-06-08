from splinter import Browser
from bs4 import BeautifulSoup
# I need this line to run chromedriver
executable_path_m = {'executable_path':r'/Users/leonardocardozo/PycharmProjects/PhilliesFangraphsDraft/chromedriver'}

NJCAA_URL ="https://www.njcaa.org/sports/bsb/teams"

new_browser = Browser('chrome', **executable_path_m)

new_browser.visit(NJCAA_URL)

new_soup = BeautifulSoup(new_browser.html, 'lxml')

schools = new_soup.find_all(class_="college-name")
print(schools)
NJCAA = []
#Get text for every school
for school in schools:
    NJCAA.append(school.text)


def college_type(school):
    if '(' and ')' in school:
        return "High School"
    elif ('JC' or 'CC') in school:
        return "2-Year"
    elif 'College' in school:
        return "2-Year"
    elif school in NJCAA: #check if school is in list
        return "2-Year"
    else:
        return "4-Year"

new_browser.quit()

