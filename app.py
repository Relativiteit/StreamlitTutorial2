""" 
# My first app 
Here's our first attempt at using data to create a table: 
"""

import streamlit as st 
import numpy as np 
import pandas as pd 

x: int = st.slider('x')

st.text_input("Your name", key ="name")


st.write(x, 'squared is', x * x )

map_data = pd.DataFrame(
    np.random.rand(1000,2) / [50, 50] + [37.76 - 122.4],
    columns=['lat', 'lon'])

st.map(map_data)

