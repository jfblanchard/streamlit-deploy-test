# More basic version of a streamlit app, just to verify functionality
# other version with neural net errors out during inference.
import streamlit as st
import pandas as pd

st.title('Streamlit app test2')

# write a dataframe and view it
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)



#%%
