from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer

#simple sentiment analysis.
testimonial = TextBlob( "Allama Khadim Hussain Rizvi New Bayan 2 Numbri Ker K ashik Rasool: https://t.co/sJRuaVQkci via @YouTube")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)

#spelling correction.
b = TextBlob("I havv goood speling!")
print(b.correct())

# Translation and Language Detection .
en_blob = TextBlob(u'Simple is better than complex.')
print(en_blob.translate(to='es'))
print(en_blob.detect_language())


#analysis with sentiment.
blob = TextBlob("I love this library",analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)

#big text analysis with separate sentences.
blob=TextBlob("What a pleasure to own iphonex.I bought it when it was launched. Checking today ...the price has dropped a 10K. Almost a year since my last upgrade. I do not compare phones. And I DO NOT compare them with Iphones. I think it is undeserving. Just saying. The camera is major on this one. The portrait mode is ace! I have the space grey in 64Gb and that's pretty much all the technical details I need. I'm one of those fortunate buyers who has the dough to spend on Apple products while residing in India so I don't really need to sit and debate with other people about why an X,Y,Z brand is better. I think Apple IS the best. Looks, functionality and everything. It does test the depth of your pockets and I think that's the only mark that there is and therefore it doesn't need comparing with other nondescript ones. I have never had any complains with any of my iphones in the past. This is my fourth upgrade. As a girl , it fulfils on the following categories - Good looks, Good looks & Good Looks. So grateful to Apple. So grateful to Amazon & so grateful to the seller. Thank you.")

#print sentiment of whole big text.
print(blob.sentiment)

#print sentiment of every sentence.
for s in blob.sentences:
    print(s)
    print(s.sentiment)

