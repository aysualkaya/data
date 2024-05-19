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


# Sort the DataFrame by country and date
df = df.sort_values(by=['country', 'date'])


# In[5]:


# Define a function to fill missing values in daily_vaccinations column
def fill_missing_vaccinations(group):
    if group['daily_vaccinations'].isnull().all():
        group['daily_vaccinations'] = 0
    else:
        group['daily_vaccinations'] = group['daily_vaccinations'].fillna(method='ffill').fillna(method='bfill').fillna(0)
    return group


# In[6]:


# Apply the function to fill missing values in daily_vaccinations column per country
df = df.groupby('country').apply(fill_missing_vaccinations)


# In[7]:


# Save the updated DataFrame to a new CSV file
df.to_csv('country_vaccination_stats_imputed.csv', index=False)


# In[ ]:




