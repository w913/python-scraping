# NicoVideoRankingSearcher(nbrs.py)

from selenium import webdriver

driver = webdriver.PhantomJS()

print("検索！カテゴリ合算 24時間 総合 ランキング（1位～300位）")
SearchWord = input("検索ワードを入力して下さい．（部分一致，入力なしで全て出力）\n> ")

driver.get("http://www.nicovideo.jp/ranking/fav/daily/all")

Title =[]
Rank = []

for i in range(3):
    Title.append(driver.find_elements_by_class_name("itemTitle"))
    Rank.append(driver.find_elements_by_class_name("rankingNum"))
    
    for j in range(len(Rank[i])):
        if(Title[i][j].text.find(SearchWord) != -1):
            print(Rank[i][j].text + "位", Title[i][j].text)
            
    if(i < 2):
        Button = driver.find_element_by_class_name("pager")
        ButtonRight= Button.find_element_by_class_name("right")
        ButtonRight.click()