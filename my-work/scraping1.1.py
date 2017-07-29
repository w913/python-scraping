from selenium import webdriver

driver = webdriver.PhantomJS()

SearchWord = "カイジ"

driver.get("http://www.nicovideo.jp/ranking/fav/daily/all")
Title = driver.find_elements_by_class_name("itemTitle")
Rank = driver.find_elements_by_class_name("rankingNum")

for i in Rank:
    i1 = int(i.text)
    if(Title[i1-1].text.find(SearchWord) != -1):
        print(i.text + "位", Title[i1-1].text)

# button = driver.find_elements_by_class_name("pager")
# button[0].click()
driver.get("http://www.nicovideo.jp/ranking/fav/daily/all?page=2")
Title2 = driver.find_elements_by_class_name("itemTitle")
Rank2 = driver.find_elements_by_class_name("rankingNum")

for i in range(len(Rank2)):
    # i1= int(i.text)
    if(Title2[i].text.find(SearchWord) != -1):
        print(Rank2[i].text + "位", Title2[i].text)

driver.get("http://www.nicovideo.jp/ranking/fav/daily/all?page=3")
Title3 = driver.find_elements_by_class_name("itemTitle")
Rank3 = driver.find_elements_by_class_name("rankingNum")

for i in range(len(Rank3)):
    # i1= int(i.text)
    if(Title3[i].text.find(SearchWord) != -1):
        print(Rank3[i].text + "位", Title3[i].text)