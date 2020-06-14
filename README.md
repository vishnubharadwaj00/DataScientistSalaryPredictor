# Data Science Salary Predictor (during COVID-19)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- Created a web application that estimates Data Science salaries (MAE~\$20k) to help data scientists better understand what salaries they might expect during COVID-19
- Webscraped job data from Glassdoor using Selenium and Chromedriver
- Feature engineered from the text of the job description to quantify the value companies place on skills like Python, R, AWS, Hadoop and many other skills, and also knowledge required typically like Algorithmic Knowledge and Statistical Knowledge.
- Optimized Linear, Lasso and Random Forest Regressors using GridsearchCV to reach the best model.
- Built a web application for users to input data and recieve an estimate, using Streamlit and Heroku.

## Motivation

During the COVID-19 pandemic, employment levels have reached new lows. The tech industry has also been affected by this, and subsequently, Data Scientists as well. Being able to get a good job right now, with a salary proportionate to the skills they possess is important, and at the same time, much more different compared to more normal period of time. This tool provides a means to help estimate how much salary one might recieve right now, based on their skills, as well as the company hiring them.

## Technologies Used

This project primarily uses Selenium 3.141.0, Numpy 1.18.3, Pandas 1.0.4, Joblib 0.15.1, Scikit_Learn 0.23.1 and Streamlit 0.61.0.

To replicate the libraries used in this project, you can run the following command:

```
pip install -r requirements.txt
```

## Environment Used

The Web Scraper code and the Streamlit code were run in a VSCode environment. The Data Cleaning, Exploratory Data Analysis and Model Building were run in a Jupyter Notebook environment.

## Models Used

Comparisions were made with a Linear Regression Model (MAE ~25K), Lasso Regression Model (MAE ~22K) and a Random Forest model (MAE ~23K), and GridSearchCV helped identify the optimal hyperparameters for tuning each of these models, attaining a Lasso Regression Model with (MAE ~20K).

## EDA Result

Some interesting results from the EDA:

![Plot1](/images/plot1.png)

![Plot2](/images/plot2.png)

![Plot3](/images/plot3.png)

![Plot4](/images/plot4.png)

## Web Application Interface

The web application was built using Streamlit and deployed using Heroku. It can be accessed at [this URL](http://ds-salary-predictor.herokuapp.com/). If I've taken it down for some reason, here's what the UI looked like:

![DSS1](/images/DSStreamlit1.png)

![DSS2](/images/DSStreamlit2.png)

## Contribute

Contributions are open from everyone.
