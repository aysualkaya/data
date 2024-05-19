#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


# Read the CSV file into a DataFrame
df = pd.read_csv('country_vaccination_stats.csv')


# In[5]:


df.head(5)


# In[9]:


# Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'])


# In[10]:


# Sort the DataFrame by country and date
df = df.sort_values(by=['country', 'date'])


# In[11]:


# Impute missing values in daily_vaccinations column with the minimum daily vaccination number of relevant countries
df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(x.min()))


# In[12]:


# Fill missing values in daily_vaccinations column for countries with no valid vaccination number yet with 0
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)


# In[13]:


# Save the updated DataFrame to a new CSV file
df.to_csv('country_vaccination_stats_imputed.csv', index=False)


# In[ ]:




