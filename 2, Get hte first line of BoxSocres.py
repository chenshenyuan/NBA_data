# usd chrome as webdriver because there is a ng-if condition when open the nba table
# so it's better to open it all even I tried wait webDriverWait


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


request_url= 'http://stats.nba.com/game/#!/0021600001/'
driver = webdriver.Chrome(executable_path='/Users/shenyuanchen/Downloads/chromedriver')

driver.get(request_url)

bsobj = BeautifulSoup(driver.page_source,'lxml')
driver.quit()
first_line= bsobj.find('div',{'class':'game-view'}).find('div',{'class':'nba-stat-table'}).find('tr').find_all('th')

for sub in first_line:
    print(sub.get_text())