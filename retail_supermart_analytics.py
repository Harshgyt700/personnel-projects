#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/charlie-aashutosh/Machine-Learning/blob/master/marketing_analytics_retail_supermart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file

# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# reading csv file
df = pd.read_csv("/content/retailData.csv")
df.head(10)


# In[3]:


# rows and cols
df.shape


# In[4]:


df.info()


# In[5]:


# check for the Missing Values.
df.isnull().sum()


# In[9]:


# deleting the column
df.drop(["Country", "Postal Code"], axis=1, inplace= True)


# In[17]:


df.columns #use chat-gpt to get KPI's


# In[11]:


# first 5 rows
df.head()


# In[18]:


# types of shipping mode
df['Ship Mode'].value_counts() #Operational Efficiency


# In[20]:


# viz
df['Ship Mode'].value_counts().plot(kind = 'bar') #Analysis of shipping type and number of customersin that category


# In[14]:


df['Segment'].value_counts().plot(kind = 'bar') # Distribution of sales across customer segments (e.g., consumer, corporate, etc.).


# In[ ]:


df['Category'].value_counts(normalize=True)


# In[21]:


df['Category'].value_counts().plot(kind = 'bar') #Breakdown of sales by product categories and sub-categories.


# - office supllies has a major part(60%) in all the transcation.

# In[22]:


df['Sub-Category'].value_counts().plot(kind = 'bar') #Breakdown of sales by product categories and sub-categories.


# ### Histogram

# In[25]:


sns.histplot(data = df, x = 'Sales') #Analysis of sales
plt.xlim(0, 500);


# In[ ]:


## filtering the data to capture sales with over 10000 USD txn
df[df['Sales']> 10000]


# In[ ]:


sns.histplot(data = df, x = 'Profit')ˀ
plt.xlim(-200, 200);


# In[ ]:


sns.histplot(data = df, x = 'Discount',bins = 20);


# In[ ]:


df.describe()


# In[ ]:


df.head()


# ## Grouping

# In[30]:


city_profit = df.groupby("City")['Profit'].sum().sort_values(ascending=False).reset_index()[:10]
city_profit


# In[31]:


sns.barplot(data = city_profit, y = 'City', x= 'Profit')


# In[32]:


plt.figure(figsize=(10, 8))

state_profit = df.groupby("State")['Profit'].sum().sort_values(ascending=False).reset_index()

sns.barplot(data = state_profit, y = 'State', x= 'Profit');


# In[33]:


state_info = df.groupby("State")[["Sales","Profit"]].sum().sort_values(by="Sales", ascending=False)[:10]
state_info


# In[34]:


state_info.plot.bar(color = ["Green","Red"], figsize=(12,6))


# In[35]:


region_info = df.groupby("Region")[["Sales","Profit"]].sum().sort_values(by="Sales", ascending=False)
region_info


# In[36]:


region_info.plot.bar(color = ["Green","Red"], figsize=(12,6))


# In[37]:


# Category wise Sales.

sns.barplot(data = df, y = 'Sales', x= 'Category')


# In[38]:


# Categories wise Profit.
sns.barplot(data = df, y = 'Profit', x= 'Category')


# In[39]:


sub_category = df.groupby('Sub-Category')['Profit'].sum().sort_values().reset_index()
sub_category[:10]


# In[40]:


sns.barplot(data=sub_category, x='Sub-Category', y='Profit')
plt.xticks(rotation = 90)
plt.title('Profit by Sub-Category');


# In[43]:


sns.lineplot(data=df, x="Category", y= "Profit")


# In[ ]:


# RCA -> root cause analysis.


# In[44]:


texas = df[df['State'] == 'Texas']
texas.head()


# In[ ]:





# In[45]:


texas['Sub-Category'].value_counts().plot(kind = 'bar')

