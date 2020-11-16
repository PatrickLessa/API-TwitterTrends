from mining import top3_words, wordsTT
from googlesearch import search
from nuvem import cloud

top3 = top3_words()
query = ''
for t3 in top3:
    for word in t3:
        query += word + " "
    
    query += "NOTICIAS"
    print(query)
    for result in search(query, lang="pt", stop=3):
        print(result)
    print("\n")
    query = ''

cloud(wordsTT())