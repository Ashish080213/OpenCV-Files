# Splitting Data for Training and Testing

from linearRegressionTemp import x, y
import numpy as np
from sklearn import model_selection

# Reshape the Data
x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

# Split the Data
xTrain, xTest, yTrain, yTest = model_selection.train_test_split(x, y, test_size=0.2)
print(xTrain.shape)





