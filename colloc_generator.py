import pymorphy2
from itertools import product
import random
morph = pymorphy2.MorphAnalyzer()

nouns = []
adjectives = []

def nouns_adjectives_selected():
    with open ('rus_shuffled.txt', 'r', encoding="UTF-8") as corpus:
        for token in corpus:
            token = token.strip()
            parsed = morph.parse(token)[0]

            if 'NOUN' in parsed.tag:
                nouns.append(parsed.normal_form)

            elif 'ADJF' in parsed.tag:
                adjectives.append(parsed.normal_form)

    random_collocations(nouns, adjectives)

def random_collocations(nouns, adjectives):
    collocations = random.choices(list(product(adjectives, nouns)))
    for colloc in collocations:
        noun = morph.parse(colloc[1])[0].tag.gender
        adj = morph.parse(colloc[0])[0]
        adj = adj.inflect({noun})
        colloc = (adj.word, colloc[1])
        print("One random ADJF - NOUN collocation: ")
        yield colloc
        continue

nouns_adjectives_selected()
collocation = random_collocations(nouns, adjectives)
for x in collocation:
    print(x)