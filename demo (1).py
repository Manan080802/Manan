#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("dataset.csv");
data


# In[3]:


data.shape


# In[4]:


len(data)


# In[5]:


data.tail(5)


# In[6]:


data.head()


# In[7]:


data.query("Address=='Ahmedabad'")


# In[8]:


data.query("Address=='Ahmedabad' & university=='GLS'")


# In[9]:


data.iloc[2:]


# In[10]:


data.iloc[[2,3,4],[2,3,4]]


# In[11]:


data.columns


# In[12]:


data.columns[1]


# In[ ]:





# In[20]:


data[data['Course ']=='MCA'].head(5)


# In[22]:


data[(data['Course ']=="MCA") & (data['gender']=="Male")]


# In[23]:


data


# In[28]:


data['pg Avgtill'].max()


# In[27]:


data['pg Avgtill'].min()


# In[29]:


data['pg Avgtill'].mean()


# In[30]:


data['pg Avgtill'].count()


# In[34]:


data['pg Avgtill'].sum()


# In[32]:


data


# In[36]:


data['gender'].replace(['Male','Female'],['M','f'])


# In[37]:


data.rename(columns={'gender':"M/F"})


# In[38]:


data[data['dob'].isnull()]


# In[39]:


data.drop([1,2])


# In[40]:


data.drop(['dob'],axis=1)


# In[ ]:




