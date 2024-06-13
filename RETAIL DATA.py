#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('D:\\dataset\\retailData.csv')


# In[3]:


data


# In[23]:


df = pd.DataFrame(data)
df


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.shape


# In[8]:


data["Ship Mode"].value_counts()


# In[9]:


data["Ship Mode"].value_counts().plot(kind = 'bar')


# In[10]:


data.Category.value_counts()


# In[11]:


data["Category"].value_counts().plot(kind = 'bar')


# In[12]:


data["Sub-Category"].value_counts()


# In[13]:


data["Sub-Category"].value_counts().plot(kind = 'bar',color = 'orange')


# In[14]:


sns.histplot(data=data, x='Sales')
plt.xlim(0,500)


# In[19]:


sns.histplot(data=data, x='Profit')
plt.xlim(-200,200)


# In[15]:


city_profit = data.groupby('City')['Profit'].sum().sort_values(ascending = False).reset_index()[:10]


# In[16]:


city_profit


# In[27]:


df =data.iloc[0:10,:]


# In[28]:


sns.barplot(data=df, y='Profit', x='City')


# In[29]:


sns.lineplot(data=df,x ='City',y ='Profit')
plt.show()


# In[33]:


region_data =data.groupby('Region')[['Sales','Profit']].sum().sort_values(by='Sales',ascending = False).reset_index()[:10]


# In[34]:


region_data


# In[35]:


region_data.plot.bar(color=['Green','Red'],figsize=(10,5))


# In[ ]:


data.head()


# In[54]:


Cat= data.groupby('Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending = False).reset_index()[:10]


# In[57]:


Category_Sale


# In[59]:


Cat.plot.bar(color=['Green','Red'],figsize=(10,5))


# In[ ]:




