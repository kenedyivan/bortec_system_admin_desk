import pandas as pd
from sklearn import preprocessing, model_selection, neighbors
import numpy as np

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['Sample code number'], 1, inplace=True)

X = np.array(df.drop(['Class'], 1))
y = np.array(df['Class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

new_sample = [4, 2, 6, 7, 4, 2, 3, 2, 1]
example_measures = np.array([new_sample])  # todo use example_measures.reshape(len(example_measures),-1)

prediction = clf.predict(example_measures)
print(prediction)
