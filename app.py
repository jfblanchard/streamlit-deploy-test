import streamlit as st

x = st.slider('Select a value to cube)
st.write(x, 'cubed is', x * x * x)
