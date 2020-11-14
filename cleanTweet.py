import re

#variavel para ajudar na exclusão de emojis dos tt
emojis = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                "]+", flags=re.UNICODE)

#limpa coisas desnecessarias do tt como menções, retweets, etc
def clean(tweet):
    tweet_clean = re.sub(r'RT+', '', tweet)
    tweet_clean = re.sub(r'#', '', tweet_clean)
    tweet_clean = re.sub(r'@\S+', '', tweet_clean)
    tweet_clean = re.sub(r'http?\S+', '', tweet_clean)
    tweet_clean = emojis.sub(r'', tweet_clean)
    tweet_clean = tweet_clean.replace("\n", "")

    return str(tweet_clean)
