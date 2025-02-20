from houserentdataload import data
from sklearn import preprocessing

# Preprocess Data
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',','')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
le = preprocessing.LabelEncoder()
data['furniture'] = le.fit_transform(data['furniture'])
print(data.head())