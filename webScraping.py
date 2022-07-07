import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(
    "C:/Users/raymo/Documents/YearUp Work/CIS 403/Project 4/chromedriver.exe")
driver.get("https://oxylabs.io/blog")
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

driver.quit()

for element in soup.find_all(attrs='css-16nzj3b esl9i4u1'):
    name = element.find('h5')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs='css-1dmex2s e1kk1ckf2'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)


df = pd.DataFrame({'Names': results, 'Genre:': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
