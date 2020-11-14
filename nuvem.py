from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

pontos = ['?', '!', '.', ',', '&',' ', '(', ')', ':', ';']
def cloud(tt):
    text = ''
    lista_teste = []

    for words in tt:
        aux = nltk.word_tokenize(words)
        lista_teste = []
        for t in aux:
            if t not in pontos:
                text += t + " "

    wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(text)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    
    plt.imshow(wordcloud)
    wordcloud.to_file("wordcloud.png")