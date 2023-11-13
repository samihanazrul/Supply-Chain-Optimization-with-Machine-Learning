#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load demand and supply data
data = pd.read_csv('demand_supply_data.csv')

# Calculate shortfall or excess
data['Shortfall_Excess'] = data['Demand'] - data['Supply']

# Suggest actions to balance demand and supply
data['Action'] = 'No Action'
data.loc[data['Shortfall_Excess'] > 0, 'Action'] = 'Increase Supply'
data.loc[data['Shortfall_Excess'] < 0, 'Action'] = 'Reduce Supply'

# Display the optimized data
print("Optimized Demand and Supply:")
print(data)


# In[ ]:




