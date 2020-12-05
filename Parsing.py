import csv
import re
import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
    page = requests.get(url)
    page.encoding = 'utf-8'
    print(page.status_code)
    parsing(page.text)

def scrolling(page):
    soup = BeautifulSoup(page, 'html.parser')
    prev_day = soup.find('a', class_='arch-arrows-link-l')
    if prev_day.findAll('href') is not None:
        link = 'https://www.newsru.com' + prev_day['href']
        new_page = requests.get(link).text
        parsing(new_page)

def parsing(page_text):
    links = []
    dates = []
    titles = []
    articles = []
    sections = []

    soup = BeautifulSoup(page_text, 'html.parser')
    if soup.find('a', href="/main/03dec2019/"):
        #print("Это новости за 3 декабря 2019!")
        # results = zip(links, dates, titles, articles, sections)
        # write_csv(results)
        # write_txt(articles)
        return 'Corpus is saved!'

    else:
        news = soup.findAll('div', class_= 'index-news-content')
        for i in range(len(news)):
            title = news[i].find(class_='index-news-title')
            title = bytes(title.text, 'utf-8').decode('utf-8', 'ignore')
            titles.append(title.strip())
            link = 'https://www.newsru.com' + news[i].find('a')['href']
            links.append(link)
            try:
                article_page = requests.get(link, timeout=15).text
                soup2 = BeautifulSoup(article_page, 'html.parser')
            except requests.exceptions.ConnectionError:
                print("Let me sleep for 5 seconds")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
            finally:
                date = soup2.find('div', class_='article-date').text
                date = re.sub(r'\s\|.*', '', date)
                date = re.sub(r'.*\:\s+', '', date)
                date = bytes(date, 'utf-8').decode('utf-8','ignore')
                dates.append(date.strip())
                section = soup2.find('a', class_='cap-link-up')
                section = bytes(section.text, 'utf-8').decode('utf-8','ignore')
                sections.append(section.strip())
                article_text = soup2.find('div', class_='article-text').find('p')
                article_text = bytes(article_text.text, 'utf-8').decode('utf-8','ignore')
                articles.append(article_text.strip())

            if i == len(news) - 1:
                res = list(zip(links, dates, titles, articles, sections))
                write_csv(res)
                write_txt(articles)
                print("News for {}:".format(date), res)
                try:
                    scrolling(page_text)
                except requests.exceptions.ConnectionError:
                    pass
                finally:
                    scrolling(page_text)

def write_csv(corpus):
    with open('NEWSRU.csv', 'a', newline='', errors='ignore') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerow(['Ссылка', 'Дата', 'Заголовок', 'Текст статьи', 'Рубрика'])
        csv_writer.writerows(corpus)

def write_txt(articles):
    with open('ARTICLES.txt', 'a', encoding="UTF-8") as f:
        for item in articles:
            f.write("%s\n" % item + "\n\n")

url = "https://www.newsru.com/allnews/"
get_html(url)