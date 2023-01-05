import streamlit as st
from PIL import Image
from fastai.vision.all import *
import fastbook
fastbook.setup_book()

path = untar_data(URLs.PETS)/'./images'

def is_cat(x): 
    return x[0].isupper()

def train_image_classifier(path):
     dls = ImageDataLoaders.from_name_func(
         path, get_image_files(path), valid_pct=0.2, seed=42,
         label_func=is_cat, item_tfms=Resize(224))

     learn = vision_learner(dls, resnet34, metrics=error_rate)
     learn.fine_tune(1)
     
     return learn


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
     image = Image.open(uploaded_file)
     st.image(image, caption='Uploaded image')


st.write('Simple Slider that computes the cube of a value')
x = st.slider('Select a value to cube')
st.write(x, 'cubed is', x * x * x)

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
    
