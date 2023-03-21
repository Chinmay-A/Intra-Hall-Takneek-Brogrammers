import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns

#reading the csv file
df = pd.read_csv("IPL 2022 Batters.csv")

#adjusting max rows to display all rows
pd.options.display.max_rows = 200

#dealing with null values
df = df.dropna()

#exploring correlations in the data
corr = df.corr()
print(corr)

data = {
  "Runs" : df.iloc[:,4],
  "HS" : df.iloc[:,5],
  "SR" : df.iloc[:,8]
}

df1 = pd.DataFrame(data)

#taking number of runs as dependent variable and number of 4s as independent variable
X = np.array(df.iloc[:,4]).reshape(-1,1)
Y = np.array(df.iloc[:,11]).reshape(-1,1)

#splitting dataset into train and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y)

#using sklearn to train our model
regr = LinearRegression()
regr.fit(x_train, y_train)

#using model to predict number of 4s for test data
y_pred = regr.predict(x_test)

plt.scatter(x_test, y_test, color ='b')
plt.plot(x_test, y_pred, color ='k')
plt.xlabel("Number of Runs")
plt.ylabel("Number of 4s")
plt.show()

MSE_test = mean_squared_error(y_test,y_pred)
print("Mean squared error for test data :"+str(MSE_test))

#MSE for train data prediction
y_pred = regr.predict(x_train)

MSE_train = mean_squared_error(y_train,y_pred)
print("Mean squared error for train data :"+str(MSE_train))


y_pred = regr.predict(x_test)
data = {
    "4s": y_test.reshape(-1),
    "Predicted 4s" : y_pred.reshape(-1)
}

#a dataframe for comparing test data with prediction data
df1 = pd.DataFrame(data)
print(df1)
