import urllib3.request, sys, time
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.thehindu.com/"
page = requests.get(URL)
# page.text gives page data along with html tags
# page.content gives page data by removing html tags so for beautiful soup give page.text as input parameter

time.sleep(2)
upper_frame=[]

soup = BeautifulSoup(page.text, 'html.parser')

mydivs = soup.findAll("div", {"class": "story-card"})
my_list = []

for st in mydivs:
    Link = st.find('a')['href'].strip()
    my_list.append(Link)

number = len(my_list)
print('Number of news articles i have now are: '+str(number))


# elements we want from each page are
# 1-> title for categorization 2-> <p> for data summarization


titles = []
paras = []
frame = []
for x in my_list:
    temp_page = requests.get(x)
    time.sleep(1)
    temp_soup = BeautifulSoup(temp_page.text, 'html.parser')
    temp_div = str(temp_soup.find("h1"))[19:-5]
    titles.append(temp_div)
    for curr_data in temp_soup.findAll("div", {"class": "paywall"}):
        paras.append(curr_data.text)
    frame.append((x, temp_div, curr_data.text))
upper_frame.extend(frame)
data = pd.DataFrame(upper_frame, columns=['Link', 'Title', 'paragraph'])
print(data.head(2))



