#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[51]:


x = pd.read_csv('C:\\Users\\Administrator\\Downloads\\train.csv')


# In[52]:


x


# In[53]:


x.describe()


# In[54]:


x.info()


# In[55]:


x.head()


# In[56]:


del x['Name']


# In[57]:


x.head()


# In[58]:


del x['Ticket']


# In[59]:


x.head()


# In[60]:


del x['Cabin']


# In[61]:


x.head()


# In[62]:


def getNumber(str):
    if str=='male':
        return 1
    else:
        return 2
x['gender']= x['Sex'].apply(getNumber)


# In[63]:


x.head()


# In[64]:


x.isnull().sum()


# In[65]:


meanS= x[x.Survived==1].Age.mean()
meanS


# In[66]:


x["age"]=np.where(pd.isnull(x.Age) & x["Survived"]==1  ,meanS, x["Age"])
x.head()


# In[67]:


x.isnull().sum()


# In[68]:


meaNS= x[x.Survived==0].Age.mean()
meaNS


# In[69]:


x.age.fillna(meaNS,inplace=True)
x.head()


# In[70]:


x.isnull().sum()


# In[71]:


def getNumber(str):
    if str=='S':
        return 1
    elif str=='Q':
        return 2
    else:
        return 3
x['embarked']= x['Embarked'].apply(getNumber)


# In[72]:


x.head()


# In[73]:


del x['Sex']


# In[74]:


del x['Embarked']


# In[75]:


del x['Age']


# In[76]:


x.head()


# In[77]:


x.rename(columns={'embarked':'Embarked'},inplace=True)
x.rename(columns={'age':'Age'},inplace=True)


# In[78]:


x.head()


# In[79]:


x.isnull().sum()


# In[84]:


males = (x.gender==1).sum()
females = (x.gender==2).sum()
p = [males,females]

plt.pie(p,
           labels=['males','females'],
           colors= ['red','green'],
           explode=(0.15,0),
           startangle=0)
plt.axis('equal')
plt.show()


# In[90]:


maleS = x[x.gender==1][x.Survived==1].shape[0]
maleN = x[x.gender==1][x.Survived==0].shape[0]
femaleS = x[x.gender==2][x.Survived==1].shape[0]
femaleN = x[x.gender==2][x.Survived==0].shape[0]
print(maleS)
print(maleN)
print(femaleS)
print(femaleN)


# In[100]:


chart=[maleS,maleN,femaleS,femaleN]
labels=['Male survived','Male dead','Female survived','Female dead']
colors=['red','green','blue','purple']
plt.pie(chart,labels=labels,colors=colors,explode=(0,0.05,0.1,0),startangle=(100),counterclock=False,autopct="%.2f%%")
plt.axis('equal')
plt.show()


# <span style=(color:'red')>
# # harah

# In[ ]:




