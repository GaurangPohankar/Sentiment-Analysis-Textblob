from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier

# traing the data accordigly 
train =[('I love this sandwich.','pos')
        ,('this is an amazing place!','pos'),
        ('I feel very good about these beers.','pos'),
        ('this is my best work.','pos')
        ,("what an awesome view",'pos'),
        ('I do not like this restaurant','neg'),
        ('I am tired of this stuff.','neg'),
        ("I can't deal with this",'neg'),
        ('he is my sworn enemy!','neg'),
        ('my boss is horrible.','neg')]

cl = NaiveBayesClassifier(train)
blob = TextBlob("The beer is good. But the hangover is horrible.",classifier=cl)
print(blob.classify())

for s in blob.sentences:
    print(s)
    print(s.sentiment)
    print(s.classify())



#classify training example how to create training data just like above 

train={}
blob=TextBlob("What a pleasure to own iphonex.I bought it when it was launched. Checking today ...the price has dropped a 10K. Almost a year since my last upgrade. I do not compare phones. And I DO NOT compare them with Iphones. I think it is undeserving. Just saying. The camera is major on this one. The portrait mode is ace! I have the space grey in 64Gb and that's pretty much all the technical details I need. I'm one of those fortunate buyers who has the dough to spend on Apple products while residing in India so I don't really need to sit and debate with other people about why an X,Y,Z brand is better. I think Apple IS the best. Looks, functionality and everything. It does test the depth of your pockets and I think that's the only mark that there is and therefore it doesn't need comparing with other nondescript ones. I have never had any complains with any of my iphones in the past. This is my fourth upgrade. As a girl , it fulfils on the following categories - Good looks, Good looks & Good Looks. So grateful to Apple. So grateful to Amazon & so grateful to the seller. Thank you.")

for s in blob.sentences:
    if s.sentiment.polarity > 0 :
        train[s] = 'Positive'
    elif s.sentiment.polarity < 0 :
        train[s] = 'Negative'
    else:
        train[s] = 'Neutral'
print(train)
