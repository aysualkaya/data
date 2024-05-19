#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Read the CSV file into a DataFrame
df = pd.read_csv('country_vaccination_stats_imputed.csv')


# In[3]:


# Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'])


# In[4]:


# Filter the DataFrame for the specified date
date_filter = df['date'] == '2021-01-06'
total_vaccinations_on_date = df[date_filter]['daily_vaccinations'].sum()


# In[5]:


print("Total vaccinations done on 2021-01-06:", total_vaccinations_on_date)


# In[ ]:




