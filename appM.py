import streamlit as st

st.title('My Streamlit App')
st.write('Hello, world!')

import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load your model
model = tf.keras.models.load_model("C:/Users/tarik/Downloads/modelKFINAL.h5")

st.title('Teeth Disease Classification')
st.write('Upload an image to classify')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    img_array = np.array(image.resize((224, 224))) / 255.0  # Adjust size as needed
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    st.write(f'Prediction: {np.argmax(prediction)}')
