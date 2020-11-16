import tweepy
import json
from cleanTweet import clean

key_consumidor = ''
secret_consumidor = ''
token = ''
secret_token = ''

auth = tweepy.OAuthHandler(key_consumidor, secret_consumidor)
auth.set_access_token(token, secret_token)
twitter = tweepy.API(auth)

def tweet():
    long_text = ''
    espaco = ' '
    lista = []

    woe_id_brazil = 23424768 #id do brasil pra ele pesquisar os trends apenas daqui
    brazil_trends = twitter.trends_place(woe_id_brazil, excluded="hashtags")
    trends50 = json.loads(json.dumps(brazil_trends, indent=1))
    trends3 = trends50[0]["trends"][0:3] #setando pra que ele me de apenas as 3 primeiras trends

    #procura os tt de cada trend
    for trend in trends3:
        word = trend["name"]
        print(word)
        result = twitter.search(q=word)

        #concatena os tt para facilitar a mineração depois
        for tweet in result:
            long_text = long_text + espaco + clean(tweet.text)
        

        lista.append(long_text)
        long_text = ''
    
    return lista


