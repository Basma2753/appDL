import streamlit as st
import subprocess
import sys

def install_tensorflow():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow"])

# Call the function to install TensorFlow
install_tensorflow()
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

