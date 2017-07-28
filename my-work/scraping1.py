from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("http://judge.u-aizu.ac.jp/onlinejudge/user.jsp?id=tozangezan#2")
text = driver.find_element_by_id("list5")
data = text.text.split("\n")
data2 = []
for i in range(len(data)-1): 
    # print(data[i].split(" "))
    data2.append(tuple(data[i].split(" ")))
print(data2)
button = driver.find_element_by_id("next_pager")
button.click()

text = driver.find_element_by_id("list5")
data = text.text.split("\n")
# for i in range(len(data)-1): 
    # print(data[i].split(" "))