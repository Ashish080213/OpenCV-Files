# Training
import sklearn.model_selection
from houserentpreprocess import data
import numpy as np
from sklearn import linear_model

# Splitting Data
print('-'*30); print("Split Data"); print('-'*30)

x = np.array(data.drop(['rent amount'], axis=1))
y = np.array(data['rent amount'])
print('X', x.shape)
print('Y', y.shape)

xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x, y, test_size=0.2, random_state=10)
print('xTrain', xTrain.shape)
print('xTest', xTest.shape)

# Training Data
print('-'*30); print("Training Data"); print('-'*30)

model = linear_model.LinearRegression()
model.fit(xTrain, yTrain)

print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')

# Accuracy
accuracy = model.score(xTest, yTest)
print(f'Accuracy: {round(accuracy*100, 3)}%')