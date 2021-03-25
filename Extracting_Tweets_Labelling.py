#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -e git+https://github.com/Mottl/GetOldTweets3#egg=GetOldTweets3')


# In[2]:


import re # regular expression / regex
import tweepy #Collect tweets
from tweepy import OAuthHandler # Authentication
from textblob import TextBlob # provides text mining, text analysis and text processing modules
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


get_ipython().system('GetOldTweets3 --querysearch "nrc" --since 2019-12-15 --until 2020-02-15 --maxtweets 600 --lang en --emoji unicode')


# In[4]:


import pandas as pd
nrc = pd.read_csv("output_got.csv")


# In[5]:


get_ipython().system('GetOldTweets3 --querysearch "caa" --since 2019-12-15 --until 2020-02-15 --maxtweets 600 --lang en --emoji unicode')


# In[6]:


caa = pd.read_csv("output_got.csv")


# In[7]:


get_ipython().system('GetOldTweets3 --querysearch "CAA_NRC" --since 2019-12-15 --until 2020-02-15 --maxtweets 600 --lang en --emoji unicode')


# In[8]:


caa_nrc = pd.read_csv("output_got.csv")


# In[9]:


get_ipython().system('GetOldTweets3 --querysearch "CAA_NRC_Protests" --since 2019-12-15 --until 2020-02-15 --maxtweets 600 --lang en --emoji unicode')


# In[10]:


caa_nrc_protests = pd.read_csv("output_got.csv")


# In[11]:


get_ipython().system('GetOldTweets3 --querysearch "citizenshipamendmentbill" --since 2019-12-15 --until 2020-02-15 --maxtweets 600 --lang en --emoji unicode')


# In[12]:


bill = pd.read_csv("output_got.csv")


# In[13]:


#indiaagainstcab
get_ipython().system('GetOldTweets3 --querysearch "indiaagainstcab" --since 2019-12-15 --until 2020-02-15 --maxtweets 600 --lang en --emoji unicode')


# In[14]:


against=pd.read_csv("output_got.csv")


# In[15]:


pList=[nrc,caa,caa_nrc,caa_nrc_protests,bill,against]
Ana_table = pd.concat(pList)
Analysis=pd.DataFrame(Ana_table['text'])
Analysis=Analysis.dropna()


# In[16]:


def sentiment_calc(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None
    


Analysis['sentiment'] = Analysis['text'].apply(sentiment_calc)


# In[17]:


Analysis['label'] = 0
Analysis.loc[Analysis['sentiment'] > 0 , 'label'] = 1
Analysis.loc[(Analysis['sentiment'] == 0), 'label'] = 0
Analysis.loc[Analysis['sentiment'] < 0, 'label'] = -1


# In[19]:


Analysis


# In[20]:


Analysis.to_csv('final.csv',index=False)


# In[ ]:





# In[ ]:





# In[ ]:




