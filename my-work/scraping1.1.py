import re
from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("http://www.nicovideo.jp/ranking/fav/daily/all")
Title = driver.find_elements_by_class_name("itemTitle")
Rank = driver.find_elements_by_class_name("rankingNum")
flag = []
# for i in Rank:
#     print(i.text)
    
#for i in Title:
#     print(i.text)

for i in Rank:
    i1= int(i.text)
    if(Title[i1-1].text.find('ゆっくり') != -1):
        print(i.text + "位", Title[i1-1].text)

# button = driver.find_element_by_class_name("pagerBtn switchingBtn right")
# button.click()

# Title = driver.find_elements_by_class_name("itemTitle")
# Rank = driver.find_elements_by_class_name("rankingNum")
# for i in Rank:
#     # print(Rank[i].text, Title[i].text)
#     if(Title[i].text.find('') != -1):
#         print(Rank.text + "位", Title[i-1].text)