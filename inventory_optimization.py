#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import networkx as nx
from geopy.distance import geodesic
import matplotlib.pyplot as plt

# Load route data
route_data = pd.read_csv('route_data.csv')

# Create a graph from the data
G = nx.Graph()

# Add nodes to the graph
for index, row in route_data.iterrows():
    G.add_node(row['location_id'], pos=(row['latitude'], row['longitude']))

# Add edges with distances as attributes
for i in range(len(route_data)):
    for j in range(i + 1, len(route_data)):
        loc1 = route_data.iloc[i]
        loc2 = route_data.iloc[j]
        distance = geodesic((loc1['latitude'], loc1['longitude']), (loc2['latitude'], loc2['longitude'])).miles
        G.add_edge(loc1['location_id'], loc2['location_id'], distance=distance)

# Solve the Travelling Salesman Problem
tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)

# Extract optimized route data
optimized_route_data = route_data[route_data['location_id'].isin(tsp_path)]

# Display the optimized route
print("Optimized Route:")
print(optimized_route_data[['location_id', 'location_name', 'latitude', 'longitude']])

# Plot the optimized route
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
plt.title('Optimized Route')
plt.show()


# In[ ]:




