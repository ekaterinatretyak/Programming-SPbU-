import csv
import re
import requests
from bs4 import BeautifulSoup

def get_html(url):
    page = requests.get(url)
    page.encoding = 'utf-8'
    print(page.status_code)
    parsing(page.text)

def parsing(page_text):
    titles = []
    covid_titles = []
    soup = BeautifulSoup(page_text, 'html.parser')

    headlines = soup.findAll('h3', class_= 'article_name')
    for i in range(len(headlines)):
        if re.findall(r'коронавирус|COVID', headlines[i].text):
            covid_titles.append(headlines[i].text)
        titles.append(headlines[i].text)
    write_csv(zip(titles))
    print("Заголовки с упоминанием коронавируса: ")
    for t in covid_titles:
        print(t)

def write_csv(corpus):
    with open('kommersant.csv', 'w', newline='', errors='ignore') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerow(['Заголовки новостных статей за октябрь 2020'])
        csv_writer.writerows(corpus)

url = "https://www.kommersant.ru/archive/rubric/4/month/2020-10-01"
get_html(url)