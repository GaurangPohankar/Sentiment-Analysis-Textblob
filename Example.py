
# importing the requests library 
import requests
import json
from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier
from pprint import pprint
  
# defining the api-endpoint  i.e. URL 
API_ENDPOINT = "http://api.plos.org/search?q=title:DNA"
  
 

# sending post request and saving response as response object 
r = requests.get(url = API_ENDPOINT) 

# extracting response text  
pastebin_url = r.text
y = json.loads(pastebin_url)

#print(y["response"]["docs"][7]["abstract"])


#print(len(y["response"]["docs"]))

train={}
for i in range(0, len(y["response"]["docs"])):
    blob=TextBlob(str(y["response"]["docs"][i]["abstract"]))
    for s in blob.sentences:
        if s.sentiment.polarity > 0 :
            train[s] = 'Positive'
        elif s.sentiment.polarity < 0 :
            train[s] = 'Negative'
        else:
            train[s] = 'Neutral'        
pprint(train)
#upload this train data using POST URL. 
