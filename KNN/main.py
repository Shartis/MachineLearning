from sklearn import datasets
import plotly.express as px
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
import math
from collections import Counter
import numpy as np


def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        distances = [distance(x, x_train) for x_train in self.X_train]
        k_idx = np.argsort(distances)[: self.k]
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]


if __name__ == '__main__':
    df = px.data.iris()
    print(df)

    figure = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
                               color="species")
    figure.show()

    normalizer = Normalizer()
    df_scaled = normalizer.fit_transform(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

    figure = px.scatter_matrix(df_scaled, dimensions=[0, 1, 2, 3], color=df['species_id'])
    figure.show()

    X_train, X_test, Y_train, Y_test = train_test_split(df_scaled,
                                                        df['species_id'].values,
                                                        test_size=0.25,
                                                   random_state=1)

    n = X_test.shape[0]

    metricas = []
    for i in range(1, 37):
        knn = KNN(k=i)
        knn.fit(X_train, Y_train)
        pred = knn.predict(X_test)
        metricas.append([accuracy(Y_test, pred), i])

    k = 0
    max_accuracy = 0
    for index_elem, elem in enumerate(metricas):

        if elem[0] > max_accuracy:
            k = elem[1]
            max_accuracy = elem[0]

    clf = KNN(k=k)
    clf.fit(X_train, Y_train)
    new_elem = clf.predict(X_test)

    figure = px.scatter_matrix(X_test, dimensions=[0, 1, 2, 3], color=new_elem)
    figure.show()

    new_elem = clf.predict([[0.714215, 0.7636, 0.69351, 0.15345]])
    print("new elem ", [[0.714215, 0.7636, 0.69351, 0.15345]])

    print("Result: ")
    if new_elem == 3:
        print("virginica")
    if new_elem == 1:
        print("setosa")
    if new_elem == 2:
        print("versicolor")
