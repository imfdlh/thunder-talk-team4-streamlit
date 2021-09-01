import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("""
# Iris Classifier App

This app predicts the type of iris flower based on its sepal and petal width and length.
""")

st.write("""
\n
""")
st.subheader('Input Data')
def user_input_features():
    sepal_length_cm = st.slider('Sepal length (cm)', 4.0, 10.0, 4.0)
    sepal_width_cm = st.slider('Sepal width (cm)', 2.0, 5.0, 2.0)
    petal_length_cm = st.slider('Petal length (cm)', 1.0, 10.0, 1.0)
    petal_width_cm = st.slider('Petal width (cm)', 0.1, 5.0, 0.1)
    
    data = {
        'sepal_length':sepal_length_cm,
        'sepal_width':sepal_width_cm,
        'petal_length':petal_length_cm,
        'petal_width':petal_width_cm
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input Features')

st.write(input_df)

model = pickle.load(open('classifier.pkl', 'rb'))

prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')
class_name = ['setosa', 'versicolor', 'virginica']
iris_class = np.array(class_name)
st.write(iris_class[prediction])
prediction_proba_df = pd.DataFrame(prediction_proba, columns=class_name)

st.subheader('Prediction Probability')
st.write(prediction_proba_df)