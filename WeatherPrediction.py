from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


weather_data = pd.read_csv('weather_data_cleaned.csv')
print(weather_data.columns)
X = weather_data.drop(columns=['Precipitation_mm'])
y = weather_data['Precipitation_mm']

#IMPORTANT: The commented out code doesn't work due to the lack of class sorting
#This commit is just to save the progress I have so far - Alex
classes = np.unique(y)
print(classes)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4524)
dt = DecisionTreeClassifier(max_depth=3);
#dt.fit(X_train, y_train)
#y_train_pred = dt.predict(X_train)
#print(accuracy_score(y_train, y_train_pred))