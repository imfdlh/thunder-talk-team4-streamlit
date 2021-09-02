import streamlit as st
import pandas as pd
import numpy as np
import pickle

# main section title
st.write("""
# Iris Classifier App

This app predicts the type of iris flower based on its sepal and petal width and length.
""")
# space only
st.write("""
\n
""")

# sidebar header
st.sidebar.header('Input Data')

# input features using function
def user_input_features():
    sepal_length_cm = st.sidebar.slider('Sepal length (cm)', 4.0, 10.0, 5.0)
    sepal_width_cm = st.sidebar.slider('Sepal width (cm)', 2.0, 5.0, 3.0)
    petal_length_cm = st.sidebar.slider('Petal length (cm)', 1.0, 10.0, 2.0)
    petal_width_cm = st.sidebar.slider('Petal width (cm)', 0.1, 5.0, 1.1)
    
    data = {
        'sepal_length':sepal_length_cm,
        'sepal_width':sepal_width_cm,
        'petal_length':petal_length_cm,
        'petal_width':petal_width_cm
    }

    features = pd.DataFrame(data, index=[0])
    return features

# call function user_input_features
input_df = user_input_features()

# subheader sidebar
st.sidebar.subheader('Links')

# link to github
st.sidebar.markdown("""
[Github Repo](https://github.com/imfdlh/thunder-talk-team4-streamlit)
""")

# subheader for main section
st.subheader('User Input Features')

# show input features in table
st.write(input_df)

# load logistic regression model
model = pickle.load(open('classifier.pkl', 'rb'))

# predict and predict proba
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# define class name
class_name = ['setosa', 'versicolor', 'virginica']
iris_class = np.array(class_name)

# save prediction proba in dataframe
prediction_proba_df = pd.DataFrame(prediction_proba, columns=class_name)

# show prediction proba table
st.subheader('Prediction Probability')
st.write(prediction_proba_df)

# show prediction result
st.subheader('Prediction')
st.write(iris_class[prediction])