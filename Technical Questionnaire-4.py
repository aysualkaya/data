#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('country_vaccination_stats_imputed.csv')


# In[3]:


# Calculate median daily vaccination numbers per country
median_daily_vaccinations = df.groupby('country')['daily_vaccinations'].median()


# In[4]:


# Sort the median daily vaccination numbers in descending order and get the top 3 countries
top_3_countries = median_daily_vaccinations.sort_values(ascending=False).head(3)


# In[5]:


print("Top 3 countries with highest median daily vaccination numbers:")
for rank, (country, median_vaccinations) in enumerate(top_3_countries.items(), start=1):
    print(f"{rank}. {country}: {median_vaccinations:.0f}")


# In[ ]:




