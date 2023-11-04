Fetch Receipt Prediction ML Model

- This project implements a machine learning model to predict the approximate number of scanned
receipts for each month of 2022 based on the observed data from 2021. Additionally, a Flask web
application is provided to interact with the trained model, allowing users to input a specific
month and year to obtain the predicted number of recipts.

PreReqs
- Python
- Flask
- NumPy

Project Structure
- app.py : Main Flask application file containing routes and logic for predicting receipts
- data/data_daily.csv : CSV file containing observed scanned receipts for the year 2021
- templates/index.html : HTML template for web interface

Usage
- Clone Repository
- Run the Flask Application (python app.py)
- Access application in your web browser at http://localhost:5000
- Enter desired month and year in provided form, click Predict to see total predicted receipts
  for specified month and year

  ML Model
  - This model is a simple Linear Regression. It uses the data from 2021 to predict receipts for
    each day of a given month. The predicted receipts are then summed up to provide a total for
    the specified month
