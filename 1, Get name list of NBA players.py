
from bs4 import BeautifulSoup
from selenium import webdriver


request_url = 'http://stats.nba.com/players/list'
historical_key = '#!?Historic=Y'
driver = webdriver.PhantomJS(executable_path='/Users/shenyuanchen/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get(request_url)

bsobj = BeautifulSoup(driver.page_source,'lxml')

name_list = bsobj.find_all('div',{'class':'large-10 columns players-list__names'})
current_name_list= []
for i in name_list:
    k = i.find_all('a')
    for w in k:
        current_name_list.append(w.text)
print(len(current_name_list))
driver = webdriver.PhantomJS(executable_path='/Users/shenyuanchen/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get(request_url+historical_key)
bsobj = BeautifulSoup(driver.page_source,'lxml')
name_list = bsobj.find_all('div',{'class':'large-10 columns players-list__names'})
historical_player_name_list= []
for i in name_list:
    k = i.find_all('a')
    for w in k:
        historical_player_name_list.append(w.text)
print(len(historical_player_name_list))




