import streamlit as st
import pandas as pd
import pickle

# Load the trained KNN model
filename = 'knn_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a title for your app
st.title('Monthly Revenue Prediction App')

# Create input fields for the user
st.header('Enter the following features:')

# Input field for feature 1 (replace with your feature names)
feature1 = st.number_input('Feature 1')

# Input field for feature 2
feature2 = st.number_input('Feature 2')


# ... (add input fields for all your features)

# Create a button to trigger prediction
if st.button('Predict Monthly Revenue'):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'Feature 1': [feature1],
        'Feature 2': [feature2],
        # ... (add your other features)
    })

    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_data)

    # Display the prediction
    st.success(f'Predicted Monthly Revenue: {prediction[0]}')
