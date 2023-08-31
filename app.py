""" 
# My first app 
Here's our first attempt at using data to create a table: 
"""

import streamlit as st 
import numpy as np 
import pandas as pd 

chart_data = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c'])

st.line_chart(chart_data)
