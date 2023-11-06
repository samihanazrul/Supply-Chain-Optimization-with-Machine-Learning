#!/usr/bin/env python
# coding: utf-8

# In[4]:


from geopy.distance import geodesic

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from geopy.distance import geodesic  # Add this line

# Load route data
route_data = pd.read_csv('route_data.csv')

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Optimized Route"])

# Home Page
if page == "Home":
    st.title("Supply Chain Optimization Dashboard")
    st.write("Welcome to the Supply Chain Optimization Dashboard. Select a page from the sidebar to explore.")

# Optimized Route Page
elif page == "Optimized Route":
    st.title("Optimized Route Visualization")
    
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

    # Plot the optimized route
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
    st.pyplot(plt)

# Run the Streamlit app


# In[ ]:




