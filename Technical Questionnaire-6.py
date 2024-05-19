#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


data = {
    'Device_Type': ['AXO145', 'AXO145', 'BPD223', 'BPD223'],
    'Stats_Access_Link': [
        'https://xcd32112.smart_meter.com/status',
        'http://abcd1234.Smart_Meter.com/data',
        'ftp://xyz_9876.Smart_Meter.com/info',
        'http://123_xyz.smart_meter.com/readings'
    ]
}


# In[3]:


# Create a DataFrame from the sample data
df = pd.DataFrame(data)


# In[6]:


# Function to extract pure URLs based on the specified rules
def extract_url(access_link):
    # Extract the URL using regex
    url_match = re.search(r'[a-z0-9_.]+\.smart_meter\.com', access_link.lower())
    if url_match:
        return url_match.group()
    else:
        return None


# In[7]:


# Process data for each device type
for device_type in df['Device_Type'].unique():
    # Filter data by device type
    device_df = df[df['Device_Type'] == device_type].copy()  # Use .copy() to avoid the warning
    
    # Extract and clean URLs
    device_df['Pure_URL'] = device_df['Stats_Access_Link'].apply(extract_url)
    
    # Display or store results
    print(f"Device Type: {device_type}")
    print(device_df[['Stats_Access_Link', 'Pure_URL']])
    print("\n")


# In[ ]:




