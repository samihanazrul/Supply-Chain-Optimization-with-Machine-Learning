#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('sales_data.csv')

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Extract useful features from the date column (e.g., month, day)
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day

# One-hot encode the 'product_type' categorical column
data = pd.get_dummies(data, columns=['product_type'], prefix='product')

# Separate features and target variable
X = data.drop(['sales', 'date'], axis=1)  # 'date' is dropped as it won't be used directly
y = data['sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the model (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
predictions = model.predict(X_test_scaled)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')
