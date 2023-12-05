# More basic version of a streamlit app, just to verify functionality
# other version with neural net errors out during inference.
import streamlit as st
import pandas as pd

# Just
a = st.sidebar.radio('Choose:',[1,2])

st.title('Streamlit app test2')

# write a dataframe and view it
st.header('Dataframe')
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)


st.write(f'The sidebar value is {a}')

st.subheader('Code Example')
st.code('for i in range(8): \n'
        '   print(i)')

st.button('Click me')
st.checkbox('Checkbox')
st.radio('Pick one:', ['left','right'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slider', min_value=0, max_value=10)
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')