!pip install -Uqq fastbook

import streamlit as st
from fastai.vision.all import *
import fastbook
fastbook.setup_book()

st.write('Simple Slider that computes the cube of a value')
x = st.slider('Select a value to cube')
st.write(x, 'cubed is', x * x * x)

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
    
