import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load the pre-trained model
model = load_model('my_malaria_cnn_model.h5')

# Function to preprocess the uploaded image
def preprocess_image(img):
    img = img.resize((30, 30))  # Resize the image to match model input dimensions
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Expand dimensions to fit model input shape
    return img

# Streamlit UI
st.title("Image Classification System")
st.write("Upload an image, and the model will predict whether it is malaria-infected or not.")

# File uploader
file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if file is not None:
    img = Image.open(file).convert('RGB')  # Open and convert the image to RGB format
    st.image(img, caption="Uploaded Image", use_column_width=True)  # Display the image
    image = preprocess_image(img)  # Process the image
    
    # Make a prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)  # Get the predicted class index
    
    # Define class labels
    class_names = ['Not Malaria', 'Malaria']
    
    # Display the result
    st.write(f"**Prediction:** {class_names[predicted_class[0]]}")
