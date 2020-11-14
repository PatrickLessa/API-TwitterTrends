from tweeter import tweet
import nltk
from collections import Counter
import json

stopwords_pt=nltk.corpus.stopwords.words('portuguese')
stopwords_en=nltk.corpus.stopwords.words('english')
pontos = ['?', '!', '.', ',', '&',' ']

def wordsTT():
    lista = tweet()
    new_list = []
    new_text = ''
    espaco = ' '

    #me retorna somente as palavras usadas em cada trend
    for text in lista:
        tokens = nltk.word_tokenize(text)
        for p in tokens:
            if p not in stopwords_pt or p not in stopwords_en:
                new_text = new_text + espaco + p

        new_list.append(new_text)
        new_text = ''

    return new_list

def top3_words():
    final_list = []
    #me retorna a quantidade de cada palavra achada
    for words in wordsTT():
        aux = nltk.word_tokenize(words)
        lista_teste = []
        for t in aux:
            if t not in pontos and len(t) > 3:
                lista_teste.append(t)

        counts = Counter(lista_teste)
        final_list.append(counts)

    #me retorna as 3 palavras mais utilizadas nos tt de cada trend
    top3 = []
    aux_list = []
    for iten in final_list:
        for keys, count in iten.most_common():
            aux_list.append(keys)
        top3.append(aux_list[0:3])
        aux_list = []

    return top3