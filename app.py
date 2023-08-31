""" 
# My first app 
Here's our first attempt at using data to create a table: 
"""

import streamlit as st 
import numpy as np 
import pandas as pd 

dataframe = np.random.rand(10,20)
st.dataframe(dataframe)

