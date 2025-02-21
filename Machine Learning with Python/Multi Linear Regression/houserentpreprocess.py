from houserentdataload import data
from sklearn import preprocessing

print('-'*30); print("Preprocessing Data"); print('-'*30)

# Preprocess Data
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',','')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
le = preprocessing.LabelEncoder()
data['furniture'] = le.fit_transform(data['furniture'])
print(data.head())

print('-'*30); print("Checking Null Data"); print('-'*30)

print(data.isnull().sum())
# data = data.dropna()

print('-'*30); print("Head Data"); print('-'*30)

print(data.head())