#!/usr/bin/env python
# coding: utf-8

# ### IMPORTING LIBRARIES

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### IGNORE WARNINGS

# In[9]:


import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)


# ### LOADING DATASET

# In[71]:


data = pd.read_csv('D:\\dataset\\FINANCIAL CSV 1.csv')


# In[82]:


data


# In[83]:


df = pd.DataFrame(data)
df


# ### DATA PREPRATION

# In[ ]:


df.describe()


# In[ ]:


df.info()


# In[ ]:


df.head(5)


# In[ ]:


df.tail(3)


# In[ ]:


type(data)


# In[ ]:


type(df['grade'])


# In[ ]:


df.index


# In[ ]:


df.columns


# In[ ]:


df.grade.values


# In[ ]:


df.set_index('id',inplace=True)


# In[26]:


df.reset_index(inplace=True)


# In[ ]:


df.head(2)


# ### DATA CLEANING
Data cleaning is a process of fixing or removing incorrect,corrupted,incorrectly formatted,duplicate or incomplete 
data within a dataset.
# ### Benefits OF Data Cleaning
Error Free Data
Accuracy and Efficiency
Data Quality
Data Consistency
# In[28]:


mask = df.isnull()


# In[ ]:


mask


# In[ ]:


print(df.isnull().sum())


# In[ ]:


df.emp_title.values


# In[ ]:


df.nunique()


# In[ ]:


df.purpose.unique()


# In[ ]:


df.verification_status.unique()


# ### DATA PERMORMING
it is a process of systematically applying the Statical, Numerical and Logical Technique to describe and illustrate 
and evaluate data
# In[ ]:


df.total_acc.max()


# In[ ]:


df['loan_amount'].min()


# In[ ]:


df['total_payment'].mode()


# In[ ]:


df.sort_values('grade')


# In[ ]:


df.iloc[0:10]


# In[ ]:


df.iloc[2:5:2]


# In[ ]:


df.nlargest(3,'annual_income')


# In[ ]:


df.


# ### DATA VISUALIZATION

# In[61]:


df.loan_status.value_counts().plot(kind='bar')
plt.title("personal loan application ",fontdict={'fontname':"Comic Sans Ms","fontsize":20})
plt.ylabel("no.of customers")


# In[62]:


df.head(5)


# In[86]:


type(df['issue_date'])


# In[93]:


df.issue_date=pd.to_datetime(df['issue_date'])


# In[95]:


df['Month'] = df['issue_date'].dt.month_name()
df.head(2)


# In[96]:


df.head(2)


# In[112]:


sns.histplot(data=df, x='loan_amount')
plt.xlim(0,500)


# In[85]:


df.head(2)


# In[108]:


df.Month.value_counts().plot(kind='bar')


# In[129]:


sns.histplot(data=df,x='Month') 


# In[ ]:


sns.lineplot(x=df["Age"],y=df["Income"],data=df) #giveing arugments for lineplot
plt.title("Age and income of customers",fontdict={"fontsize":20})  #labelling the tittle and font
plt.figure(figsize=(10,6),dpi=300)  #giving figure measurments
plt.savefig("lineplot",dpi=300) #command to save figure
plt.show()  #it stops displaying the plotname etc..


# In[110]:


df.head(2)


# In[115]:


df.nunique()


# In[118]:


sns.displot(df["emp_length"],kde=True,height=7,aspect=3,color='red')
plt.show()


# In[146]:


Fully_Paid = df.loc[df["loan_status"]==1].count()[0]#splitting undergrad data from data
Current = df.loc[df["loan_status"]==2].count()[0]#splitting graduate data from data
Charged_Off = df.loc[df["loan_status"]==3].count()[0]#splitting proffesional data from data
labels=["Fully Paid,Current,Charged Off"] #giving labels paramerts in graph
Status=[Fully_Paid,Current,Charged_Off] #giving argument for x
plt.pie(x=Status,data=df,labels=labels,autopct="%2F.%%") #plotting pie chart by passing arguments
plt.title("Loan Status of Customers",fontdict={"fontsize":20,"fontname":"comic sans MS"}) #giving title to the graph
plt.figure(figsize=(5,8),dpi=300) #most common dpi is 300
plt.show()


# In[147]:


df.loan_status.value_counts()


# In[140]:


df['loan_status'] = df['loan_status'].replace('Fully Paid','Fully_Paid')


# In[144]:


df['loan_status'] = df['loan_status'].replace('Charged Off','Charged_Off')


# In[151]:


sns.barplot(data=df, y='loan_status', x='loan_amount')


# In[ ]:




