""" 
# My first app 
Here's our first attempt at using data to create a table: 
"""

import streamlit as st 
import numpy as np 
import pandas as pd 

df = pd.DataFrame({ 
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['second column'],
)

'You selected: ', option 
