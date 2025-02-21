# Evaluation
from houserenttraining import model, xTest, yTest

print('-'*30); print("Manual Testing"); print('-'*30)

testvals = model.predict(xTest)
print(testvals.shape)

error = []
for i, testval in enumerate(testvals):
    error.append(yTest[i] - testval)
    print(f'Actual: {yTest[i]} Prediction: {int(testval)} Error: {int(error[i])}')