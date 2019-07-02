# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:08:24 2019

@author: s534846
"""

import tweepy
import csv
#import pandas as pd
#import datetime
from twitter_keys import consumer_key, consumer_secret, access_token, access_secret
#import pickle
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)


#Azure 

csvFile = open('azure.csv', 'w')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Azure",
                           lang="en").items(100):
    #print (tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
    

    
from nltk_helper import get_sentiments
    


for tweet in tweepy.Cursor(api.search,q="#Azure",
                           lang="en").items(100):
    print("Azure tweets : ",get_sentiments(tweet.text))
print()


Azure=tweepy.Cursor(api.search,q="#Azure",
                           lang="en").items(100)


# salesforce

csvFile = open('salesforce.csv', 'w')

csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#salesforce",
                           lang="en").items(100):
    #print (tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
    

    
from nltk_helper import get_sentiments
    


for tweet in tweepy.Cursor(api.search,q="#salesforce",
                           lang="en").items(100):
    print("salesforce tweets : ",get_sentiments(tweet.text))
print()


salesforce=tweepy.Cursor(api.search,q="#salesforce",
                           lang="en").items(100)


#AWS

csvFile = open('AWS.csv', 'w')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#AWS",
                           lang="en").items(100):
    #print (tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
    

    
from nltk_helper import get_sentiments
    

for tweet in tweepy.Cursor(api.search,q="#AWS",lang="en").items(100):
                           
                           print("AWS tweets : ",get_sentiments(tweet.text))
    
print()


AWS=tweepy.Cursor(api.search,q="#AWS",
                           lang="en").items(100)












from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


#build our figure
fig = plt.figure()
#build axes
ax=fig.add_subplot(111,projection='3d')

sentiments = [get_sentiments(tweet.text) for tweet in Azure]


xs=[]
for sent in sentiments:
    xs.append(sent['neg'])
    
ys=[sent['neu'] for sent in sentiments]

zs = list(map(lambda x:x['pos'],sentiments))

ax.scatter(xs,ys,zs)






#**********************************************************************************************************



from nltk_helper import split_sentiments

vX,vY,vZ = split_sentiments([get_sentiments(tweet.text) for tweet in tweepy.Cursor(api.search,q="#salesforce",
                           lang="en").items(100)])
  
ax.scatter(vX,vY,vZ, color='r',marker='*')
#ax.scatter(arbyX,arbyY,arbyZ)

#ax.scatter(xs,ys,zs)
ax.set_xlabel('Negative')
ax.set_ylabel('neutral')
ax.set_zlabel('postive')




zX,zY,zZ = split_sentiments([get_sentiments(tweet.text) for tweet in tweepy.Cursor(api.search,q="#AWS",
                           lang="en").items(100)])
ax.scatter(zX,zY,zZ, color='g',marker='d')
ax.scatter(zX,zY,zZ)

ax.scatter(xs,ys,zs)
ax.set_xlabel('Negative')
ax.set_ylabel('neutral')
ax.set_zlabel('postive')

plt.show()


#**********************************************************************************************************


from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

positive1 = []
negative1 = []
neutral1 = []
for tweet in tweepy.Cursor(api.search,q="#Azure",
                           lang="en").items(100):   
    if(analyzer.polarity_scores(tweet.text)['compound']) >=0.5:        
        positive1.append(tweet.text)
    elif(analyzer.polarity_scores(tweet.text)['compound']) <= -0.5:        
        negative1.append(tweet.text)
    else:
        neutral1.append(tweet.text) 
        

        
positive2 = []
negative2 = []
neutral2 = []       
for tweet in tweepy.Cursor(api.search,q="#salesforce",
                           lang="en").items(100):   
    if(analyzer.polarity_scores(tweet.text)['compound']) >=0.5:        
        positive2.append(tweet.text)
    elif(analyzer.polarity_scores(tweet.text)['compound']) <= -0.5:        
        negative2.append(tweet.text)
    else:
        neutral2.append(tweet.text)  

positive3 = []
negative3 = []
neutral3 = []
for tweet in tweepy.Cursor(api.search,q="#AWS",
                           lang="en").items(100):   
    if(analyzer.polarity_scores(tweet.text)['compound']) >=0.5:        
        positive3.append(tweet.text)
    elif(analyzer.polarity_scores(tweet.text)['compound']) <= -0.5:        
        negative3.append(tweet.text)
    else:
        neutral3.append(tweet.text)           


print()
total1=len(positive1)+len(negative1)+len(neutral1)
per_pos1=len(positive1)/total1*100
per_neg1=len(negative1)/total1*100
per_neu1=len(neutral1)/total1*100

print('length of positive tweets for Azure: ',per_pos1)
print('length of negative tweets for Azure: ',per_neg1)
print('length of neutral tweets for Azure: ',per_neu1)



total2=len(positive2)+len(negative2)+len(neutral2)
per_pos2=len(positive2)/total2*100
per_neg2=len(negative2)/total2*100
per_neu2=len(neutral2)/total2*100

print('length of positive tweets for salesforce: ',per_pos2)
print('length of negative tweets for salesforce: ',per_neg2)
print('length of neutral tweetsfor salesforce: ',per_neu2)

print(positive2)
print(negative2)
print(neutral2)


total3=len(positive3)+len(negative3)+len(neutral3)
per_pos3=len(positive3)/total3*100
per_neg3=len(negative3)/total3*100
per_neu3=len(neutral3)/total3*100

print('length of positive tweets for AWS: ',per_pos2)
print('length of negative tweets for AWS : ',per_neg2)
print('length of neutral tweets for AWS: ',per_neu2)

print(positive3)
print(negative3)
print(neutral3)

import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.1
 
# set height of bar
'''
postiveFinal = [per_pos1,per_pos2,per_pos3]
negativeFinal = [per_neg1, per_neg2, per_neg3]
neutralFinal = [per_neu1, per_neu2, per_neu3]
'''
postiveFinal = [per_pos1,per_neg1,per_neu1]
negativeFinal = [per_pos2, per_neg2, per_neu2]
neutralFinal = [per_pos3, per_neg3, per_neu3]
 
print(postiveFinal)

fig = plt.figure()

plt.ylim(0, 100)

n=3

index=np.arange(n)

barwidth=0.25

opacity=0.8

 

 

objects=('Postive','Negative','Neutral')

 

rects1 = plt.bar(index, postiveFinal, barwidth,

alpha=opacity,

color='o',

label='Azure')

 

rects2 = plt.bar(index + barwidth, negativeFinal, barwidth,

alpha=opacity,

color='y',

label='salesforce')

 

 

rects3 = plt.bar(index +barwidth+ barwidth, neutralFinal, barwidth,

alpha=opacity,

color='b',

label='AWS')

 

 



plt.xticks(index + barwidth,objects)

plt.ylabel('units in percentage (%)')
plt.xlabel(' POLARITY CLASSIFICATION')           
           

plt.title('Trending Cloud Service Provider')
  

plt.legend()

plt.tight_layout()



 

plt.show()




