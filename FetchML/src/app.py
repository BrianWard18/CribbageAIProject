from flask import Flask, request, render_template
import csv
import datetime
import numpy as np

app = Flask(__name__)

# Load and preprocess the data
data = []
with open('data/data_daily.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
        receipt_count = int(row[1])
        data.append((date, receipt_count))

# Feature Engineering
processed_data = []
for date, receipt_count in data:
    month = date.month
    day = date.day
    processed_data.append((month, day, receipt_count))

# Model Training (Simple Linear Regression from scratch)
X = np.array([(month, day) for month, day, _ in processed_data])
y = np.array([receipt_count for _, _, receipt_count in processed_data])

# Add bias term to X for linear regression
X_with_bias = np.c_[np.ones(X.shape[0]), X]

# Calculate weights using closed-form solution of linear regression
weights = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = int(request.form['year'])
    month = int(request.form['month'])

    # Assuming 31 days in each month for simplicity
    days_in_month = 31
    total_predicted_receipts = 0
    for day in range(1, days_in_month + 1):
        X_pred = np.array([1, month, day])  # Include bias term
        predicted_receipts = X_pred @ weights
        total_predicted_receipts += predicted_receipts

    return f'Total predicted receipts for {month}/{year}: {total_predicted_receipts:.0f}'

if __name__ == '__main__':
    app.run(debug=True)