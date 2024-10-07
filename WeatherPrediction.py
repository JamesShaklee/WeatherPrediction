from sklearn.metrics import accuracy_score, r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


weather_data = pd.read_csv('weather_data_cleaned.csv')
print(weather_data.columns)
X = weather_data.drop(columns=['Precipitation_mm', 'Rain_Category', 'Date_Time', 'Location', 'Date', 'Time', 'Millitary_Time'])
y = weather_data['Precipitation_mm']

#IMPORTANT: The commented out code doesn't work due to the lack of class sorting
#This commit is just to save the progress I have so far - Alex

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print('X_train.shape = ', X_train.shape)
print('y_train.shape = ', y_train.shape)
print('X_test.shape = ', X_test.shape)
print('y_test.shape = ', y_test.shape)
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
y_train_pred = dt.predict(X_train)
print(r2_score(y_train, y_train_pred))
y_test_pred = dt.predict(X_test)
print(r2_score(y_test, y_test_pred))