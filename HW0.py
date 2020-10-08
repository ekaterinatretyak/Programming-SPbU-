import re
import csv
import nltk
from collections import defaultdict
from pymystem3 import Mystem
import urllib
from bs4 import BeautifulSoup
import json

m = Mystem()
i = 0
d = defaultdict(int)
d2 = defaultdict(int)

with open('dom.txt', encoding='UTF-8') as data:
    dom = str(data.read()).lower()
    res = re.sub(r'[^\w\s]', '', dom)
    tokens = nltk.word_tokenize(res)
    words = [word for word in tokens]
    for item in words:
        d[item] += 1

with open('freq_dict.csv', 'w', encoding='windows-1251', newline='') as freqDict:
    csv_writer = csv.writer(freqDict, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    csv_writer.writerow(['Word', 'Frequency', 'Rank'])
    for item in sorted(d, key=d.get, reverse=True):
        i += 1
        results = [item, d[item], i]
        csv_writer.writerow(results)
    freqDict.close()

lemmas = m.lemmatize(res)
lemmas = [lemma for lemma in lemmas if lemma.strip().isalpha()]
for lem in lemmas:
   print(lem)
print([lem for lem in lemmas if lem.count('о') == 2])

url = 'http://lib.ru/POEZIQ/PESSOA/lirika.txt'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.extract()

text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk).lower()
dataWeb = re.sub(r'[^\w\s]', '', text)

tokens2 = nltk.word_tokenize(dataWeb)
words2 = [word for word in tokens2]
for wrd in words2:
    d2[wrd] += 1

with open ("freq_dict.json", "w", encoding = "utf-8") as out_file:
    for wrd in sorted(d2, key=d2.get, reverse=True):
        json.dump({wrd:d2[wrd]}, out_file, ensure_ascii=False, separators=('', ':'), indent=1)

    out_file.close()