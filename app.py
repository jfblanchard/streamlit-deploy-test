import streamlit as st
from PIL import Image
# from fastai.vision.all import *
# import fastbook
# fastbook.setup_book()

# path = untar_data(URLs.PETS)/'./images'

# should be in current directory
with open('./test.txt','r') as f:
    test_text = f.read()
    
st.write(test_text)

# functions
def is_cat(x): 
    return x[0].isupper()

# def train_image_classifier(path):
#      dls = ImageDataLoaders.from_name_func(
#          path, get_image_files(path), valid_pct=0.2, seed=42,
#          label_func=is_cat, item_tfms=Resize(224))

#      learn = vision_learner(dls, resnet34, metrics=error_rate)
#      learn.fine_tune(1)
     
#      return learn

# Create UI
st.markdown('<h2><center>Cat/Dog Image Classifier</center></h2>', unsafe_allow_html=True)  # or try st.header()
uploaded_file = st.file_uploader("Choose an image file of a cat or dog")

# only shows up when a file is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image')

    st.write('Training...')  # later use tqdm.... Or load the pretrained model
    # learn = train_image_classifier(path)
    # st.write('Done Training')

    # is_cat,_,probs = learn.predict(image)
    # st.write(f"Is this a cat?: {is_cat}.")
    # st.write(f"Probability it's a cat: {probs[1].item():.6f}")

st.write('Have a great day!')
# Other gui stuff
# st.write('Simple Slider that computes the cube of a value')
# x = st.slider('Select a value to cube')
# st.write(x, 'cubed is', x * x * x)

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
    
