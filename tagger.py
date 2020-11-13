from corus import load_corpora
import tqdm
import wget
import re
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
import collections
import pickle

wget.download('http://opencorpora.org/files/export/annot/annot.opcorpora.xml.byfile.zip')
path = 'annot.opcorpora.xml.byfile.zip'
records = load_corpora(path)

with open('pos_data.txt', 'w', encoding='utf8') as f:
    for rec in tqdm.tqdm(records):
        for par in rec.pars:
            for sent in par.sents:
                for token in sent.tokens:
                    f.write(f'{token.text} {token.forms[0].grams[0]}\n')

class UnigramMorphAnalyzer:
    def __init__(self, corpus):
        self.corpus = list(open(corpus, 'r', encoding="UTF-8").read().split("\n"))
        self.endings_stat = {}
        self.x_train, self.x_test = train_test_split(self.corpus, shuffle=False, test_size=0.2)

    def __getitem__(self, key):
        return self.endings_stat[key]

    def train(self):
        endings = {}
        pairs = []
        print("Объем данных для обучения:", len(self.x_train))
        print("Объем тестовых данных:", len(self.x_test), "\n")

        for el in self.x_train:
            tokens = []
            pos = []
            el = el.split(" ")
            tokens.append(el[0])
            pos.append(el[1])

            for token in tokens:
                for i in reversed(range(5)[1:5]):
                    ending = token[-i:]
                    pair = (ending, el[1])
                    pairs.append(pair)
                    if len(token) == i:
                        break

        c = collections.Counter()
        for pair in pairs:
            c[pair] += 1
            endings = {pair[0]: {pair[1]: c[pair]}}
            if pair[0] not in self.endings_stat:
                self.endings_stat[pair[0]] = {pair[1]: c[pair]}
            else:
                self.endings_stat[pair[0]].update({pair[1]: c[pair]})

    def predict(self, word):
        probabilities = {}
        for i in reversed(range(5)[1:5]):
            ending = word[-i:]
            if ending in self.endings_stat:
                for key in self.endings_stat[ending]:
                    probability = self.endings_stat[ending].get(key) / sum(self.endings_stat[ending].values())
                    probabilities.update({key: probability})
            return probabilities
            break
        self.save()

    def save(self):
        with open('tagger_model.pkl', 'wb') as output:
            model = UnigramMorphAnalyzer('pos_data.txt')
            pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open('tagger_model.pkl', 'rb') as input:
            model = pickle.load(input)

    def eval(self):
        correct_predictions = 0
        for x_true in self.x_test:
            x_true = x_true.split(" ")
            for a in reversed(range(5)[1:5]):
                ending = x_true[0][-a:]
                if ending in self.endings_stat:
                    keys = list(self.endings_stat[ending].keys())
                    vals = list(self.endings_stat[ending].values())
                    x_pred = keys[vals.index(max(vals))]
                    if x_pred == x_true[1]:
                        correct_predictions += 1
                        break
                    else:
                        continue

        accuracy = correct_predictions / len(self.x_test)
        return accuracy

example = UnigramMorphAnalyzer('pos_data.txt')
example.train()
print("POS-possibility for given token: ", example.predict("грация"))
print("POS-statistics for given token: ", example["рит"])
print("Accuracy: ", example.eval())