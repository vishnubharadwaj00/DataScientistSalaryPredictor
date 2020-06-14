import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sklearn


df = pd.read_csv('glassdoor_jobs_cleaned.csv')

st.title('Data Science Salary Predictor (during COVID-19)')

model = joblib.load('model.pkl')

st.markdown(
    "## All fields are mandatory.")

st.subheader('Company Details: \n Check Glassdoor for exact values, if unsure')

rating = st.slider('Glassdoor Rating of the Company',
                   min_value=0.0, max_value=5.0, step=0.1)
age = st.number_input('Age of the Company', step=1.0, min_value=0.0)
num_comp = st.number_input('Number of Competitors', step=1.0, min_value=0.0)

st.subheader('Details about the Job:')

jobhq = st.radio(
    "Is the Job at Headquarters? (0 for No, 1 for Yes)", options=[0, 1])
job_type_num = st.selectbox("Job Type",
                            options=df["job_type"].unique())


def number_simplifier(role):
    if role == "data scientist":
        return 3
    elif role == "data engineer":
        return 2
    elif role == "analyst":
        return 1
    elif role == "director":
        return 4
    elif role == "manager":
        return 5
    elif role == "mle":
        return 6
    elif role == "na":
        return 7
    elif role == "research":
        return 8
    elif role == "sw":
        return 9


job_type_num1 = number_simplifier(job_type_num)


def senior_simplifier(title):
    if title == "Senior":
        return 1
    else:
        return 2


seniority_num = st.radio("Senior role?", options=["Senior", "Not Senior"])
seniority_num1 = senior_simplifier(seniority_num)

len_desc = st.number_input('Character Length of the Job Description', step=1.0)

st.subheader('Your skills:')
python_yn = st.radio("Python (0 for No, 1 for Yes)", options=[0, 1])
r_yn = st.radio("R (0 for No, 1 for Yes)", options=[0, 1])
aws_yn = st.radio("AWS (0 for No, 1 for Yes)", options=[0, 1])
spark_yn = st.radio("Spark (0 for No, 1 for Yes)", options=[0, 1])
hadoop_yn = st.radio("Hadoop (0 for No, 1 for Yes)", options=[0, 1])
docker_yn = st.radio("Docker (0 for No, 1 for Yes)", options=[0, 1])
sql_yn = st.radio("SQL (0 for No, 1 for Yes)", options=[0, 1])
linux_yn = st.radio("Linux (0 for No, 1 for Yes)", options=[0, 1])
flask_yn = st.radio("Flask (0 for No, 1 for Yes)", options=[0, 1])
django_yn = st.radio("Django (0 for No, 1 for Yes)", options=[0, 1])
tensorflow_yn = st.radio("Tensorflow (0 for No, 1 for Yes)", options=[0, 1])
keras_yn = st.radio("Keras (0 for No, 1 for Yes)", options=[0, 1])
pytorch_yn = st.radio("PyTorch (0 for No, 1 for Yes)", options=[0, 1])
tableau_yn = st.radio("Tableau (0 for No, 1 for Yes)", options=[0, 1])
algo_yn = st.radio(
    "Strong Algorithmic Knowledge (0 for No, 1 for Yes)", options=[0, 1])
stats_yn = st.radio(
    "Strong Statistical Knowledge (0 for No, 1 for Yes)", options=[0, 1])


features = [rating, jobhq,  age, num_comp,  python_yn, r_yn, aws_yn, spark_yn, hadoop_yn,
            docker_yn, sql_yn, linux_yn, flask_yn, django_yn, tensorflow_yn, keras_yn,
            pytorch_yn, tableau_yn, algo_yn, stats_yn, job_type_num1, seniority_num1, len_desc]
final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(final_features)
    st.balloons()
    st.success(f'Your predicted salary is US$ {round(prediction[0],3)*1000} ')
