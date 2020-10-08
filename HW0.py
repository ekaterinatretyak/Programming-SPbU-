import re
import csv
import nltk
from collections import defaultdict
from pymystem3 import Mystem
import urllib
from bs4 import BeautifulSoup
import json

m = Mystem()
d = defaultdict(int)
d2 = defaultdict(int)

def file_processing(data):

    """
    This function allows us to work with a text file and do basic text processing.
    After that the function makes a frequency dictionary of the text words.

    :param data: the path to the file with an original text
    """

    # We open and read the file 'dom.txt',
    # convert text to lowercase and delete all the punctuation.
    dom = data.read().lower()
    res = re.sub(r'[^\w\s]', '', dom)

    # To make a frequency dictionary we need to tokenize the text
    # and to count a frequency of each word in the text
    tokens = nltk.word_tokenize(res)
    words = [word for word in tokens]
    for item in words:
        d[item] += 1

    # Now we lemmatize the text via pyMystem
    # and find all the lemmas with exactly 2 letters "o"
    lemmas = m.lemmatize(res)
    lemmas = [lemma for lemma in lemmas if lemma.strip().isalpha()]
    for lem in lemmas:
        print(lem)
    print([lem for lem in lemmas if lem.count('о') == 2])


def write_to_csv(freqDict):

    """
    This function creates a CSV file and writes the derived frequency dictionary in the file
    @:param freqDict: the path to the CSV file
    """

    # We create a CSV file and write down three columns: 'Word', 'Frequency' and 'Rank'
    i = 0 # variable for rank
    csv_writer = csv.writer(freqDict, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    csv_writer.writerow(['Word', 'Frequency', 'Rank'])

    # After ranking the words in order of decreasing their frequencies, we write the meanings into the table
    for item in sorted(d, key=d.get, reverse=True):
       i += 1
       results = [item, d[item], i]
       csv_writer.writerow(results)

# We open the link and read all the text from the web page
def parsing(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk).lower()

    # Delete all the punctuation, tokenize the text and count word frequencies in the text
    dataWeb = re.sub(r'[^\w\s]', '', text)
    tokens2 = nltk.word_tokenize(dataWeb)
    words2 = [word for word in tokens2]
    for wrd in words2:
        d2[wrd] += 1

def write_to_json(out_file):
    """
    This function creates a JSON file and writes down there a dictionary of the form: {word: frequency}
    :param out_file: the path to the JSON file
    """
    for wrd in sorted(d2, key=d2.get, reverse=True):
        json.dump({wrd:d2[wrd]}, out_file, ensure_ascii=False, separators=('', ':'), indent=1)

    out_file.close()

file_processing(open('dom.txt', 'r', encoding="utf-8"))
write_to_csv(open('freq_dict.csv', 'w', encoding='windows-1251', newline=''))
parsing(url='http://lib.ru/POEZIQ/PESSOA/lirika.txt')
write_to_json(open('freq_dict.json', 'w', encoding = "utf-8"))