# Creating Linear Regression Model

from datasplitting import xTrain, yTrain, xTest, yTest
from sklearn import linear_model

model = linear_model.LinearRegression()
model.fit(xTrain, yTrain)
print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')

accuracy = model.score(xTest, yTest)
print(f'Accuracy: {accuracy*100}')