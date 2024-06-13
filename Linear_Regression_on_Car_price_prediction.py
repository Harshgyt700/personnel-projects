#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snr


# Step 1 : Gathering the data

# In[2]:


data=pd.read_csv("C:\\Users\\Administrator\\Downloads\\data.csv")


# In[3]:


data.head()


# In[4]:


plt.figure(figsize=(10,10))
snr.countplot(y=data.Make)
plt.title("Brands with the number of cars manufactured",fontsize=20)
plt.show()


# In[5]:


plt.figure(figsize=(10,10))
snr.countplot(x='Vehicle Size',data=data,palette='Set1')
plt.title("Count of manufactured vehicles based on Vehicle size",fontsize=20)


# In[6]:


plt.figure(figsize=(10,10))
snr.countplot(x='Transmission Type',data=data,palette='Set1')


# In[7]:


plt.figure(figsize=(10,10))
data.groupby('Transmission Type')['MSRP'].mean().plot(kind='bar')
plt.title("Average price of cars in different transmission types",fontsize=20)
plt.show()


# In[8]:


data.info()


# Step 2 : Data preprocessing

# In[9]:


#converting the categorical variables into numeric format -- LabelEncoder
from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()


# In[10]:


data['Engine Fuel Type'].unique()


# In[11]:


data['Engine Fuel Type']=label_encoder.fit_transform(data['Engine Fuel Type'])


# In[12]:


data['Engine Fuel Type'].unique()


# In[13]:


data['Make'].unique()


# In[14]:


data['Make']=label_encoder.fit_transform(data['Make'])


# In[15]:


data['Make'].unique()


# In[16]:


data['Model'].unique()


# In[17]:


data['Model']=label_encoder.fit_transform(data['Model'])


# In[18]:


data['Model'].unique()


# In[19]:


data['Transmission Type'].unique()


# In[20]:


data['Transmission Type']=label_encoder.fit_transform(data['Transmission Type'])


# In[21]:


data['Transmission Type'].unique()


# In[22]:


data['Driven_Wheels'].unique()


# In[23]:


data['Driven_Wheels']=label_encoder.fit_transform(data['Driven_Wheels'])


# In[24]:


data['Driven_Wheels'].unique()


# In[25]:


data['Market Category'].unique()


# In[26]:


data['Market Category']=label_encoder.fit_transform(data['Market Category'])


# In[27]:


data['Market Category'].unique()


# In[28]:


data['Vehicle Size'].unique()


# In[29]:


data['Vehicle Size']=label_encoder.fit_transform(data['Vehicle Size'])


# In[30]:


data['Vehicle Size'].unique()


# In[31]:


data['Vehicle Style'].unique()


# In[32]:


data['Vehicle Style']=label_encoder.fit_transform(data['Vehicle Style'])


# In[33]:


data['Vehicle Style'].unique()


# In[34]:


data.head()


# In[35]:


#checking for null values in the dataset
data.isnull().sum()


# In[36]:


data['Engine HP']=data['Engine HP'].fillna(data['Engine HP'].mode()[0])
data['Engine Cylinders']=data['Engine Cylinders'].fillna(data['Engine Cylinders'].mode()[0])
data['Number of Doors']=data['Number of Doors'].fillna(data['Number of Doors'].mode()[0])


# In[37]:


data.isnull().sum()


# Step 3 : Dividing the data into X and y

# In[38]:


X=data.drop(['MSRP'],axis=1) #independent variables
y=data['MSRP'] #dependent variables


# In[39]:


X.head()


# Step 4 : Splitting the data into training and testing set

# In[40]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15) #15% of the data used for testing


# In[41]:


from sklearn.linear_model import LinearRegression
regression=LinearRegression()


# In[42]:


regression.fit(X_train,y_train) #fit() helps in training the model


# In[43]:


y_hat=regression.predict(X_test)#.predict() helps in predicting the o/p from the MLM


# In[44]:


#accuracy of the model using R2 Score
regression.score(X,y)


# In[45]:


#other algos we can expore -- support vector regressor, decision tree regressor, random forest regressor


# In[46]:


#computing mean absolute error and mean squared error
from sklearn.metrics import mean_squared_error, mean_absolute_error
mean_squared_error=mean_squared_error(y_hat,y_test)
mean_absolute_error=mean_absolute_error(y_hat,y_test)


# In[47]:


print(mean_squared_error) #np.sqrt(mean_squared_error) --> RMSE


# In[48]:


print(mean_absolute_error)


# In[ ]:




