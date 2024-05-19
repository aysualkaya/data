#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_excel('DailyActivities.xlsx')


# In[11]:


df.head(10)


# In[7]:


import matplotlib.pyplot as plt


# In[24]:


# Calculate total hours for each person
total_susan = df['Susan'].sum()
total_henry = df['Henry'].sum()
total_charles = df['Charles'].sum()

# Plotting
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

for i, (person, total) in enumerate(zip(['Susan', 'Henry', 'Charles'], [total_susan, total_henry, total_charles])):
    ax = axes[i]
    ax.pie(df[person], labels=df['Area of Interest'], autopct='%1.1f%%', startangle=90)
    ax.set_title(person + '\'s Daily Activities\nTotal Hours: {}'.format(total))
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.show()


# In[17]:


plt.figure(figsize=(10, 6))

plt.bar(df['Area of Interest'], df['Susan'], label='Susan')
plt.bar(df['Area of Interest'], df['Henry'], bottom=df['Susan'], label='Henry')
plt.bar(df['Area of Interest'], df['Charles'], bottom=df['Susan'] + df['Henry'], label='Charles')

plt.xlabel('Area of Interest')
plt.ylabel('Hours')
plt.title('Unified Daily Activities')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[23]:


bar_width = 0.25
index = df.index
susan = plt.bar(index - bar_width, df['Susan'], bar_width, label='Susan')
henry = plt.bar(index, df['Henry'], bar_width, label='Henry')
charles = plt.bar(index + bar_width, df['Charles'], bar_width, label='Charles')

plt.xlabel('Area of Interest')
plt.ylabel('Hours')
plt.title('Unified Daily Activities')
plt.xticks(index, df['Area of Interest'])
plt.legend()

plt.tight_layout()
plt.show()

