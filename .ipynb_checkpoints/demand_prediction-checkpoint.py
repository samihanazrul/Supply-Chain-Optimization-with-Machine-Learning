{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bf9a4841",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error: 24.82594729119432\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "\n",
    "# Assuming 'your_dataset.csv' is the name of your dataset\n",
    "data = pd.read_csv('sales_data.csv')\n",
    "\n",
    "# One-hot encode categorical variables like 'feature1' and 'feature2'\n",
    "data = pd.get_dummies(data, columns=['feature1', 'feature2'], prefix=['feat1', 'feat2'])\n",
    "\n",
    "# Separate features and target variable\n",
    "X = data.drop('target_variable', axis=1)\n",
    "y = data['target_variable']\n",
    "\n",
    "# Split the data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Initialize the model (Random Forest Regressor in this case)\n",
    "model = RandomForestRegressor(n_estimators=100, random_state=42)  # You can adjust hyperparameters here\n",
    "\n",
    "# Train the model\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Make predictions on the test set\n",
    "predictions = model.predict(X_test)\n",
    "\n",
    "# Evaluate the model\n",
    "mae = mean_absolute_error(y_test, predictions)\n",
    "print(f'Mean Absolute Error: {mae}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f782b68",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
