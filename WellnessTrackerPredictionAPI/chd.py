import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
import sklearn


def chdprediction():    
    df = pd.read_csv('./dataset/customdataset.csv')
    df.head()
    df.info()
    df.corr().T
    x = df[["heartrate","bloodpressure","cholesterol"]]
    y = df[["outcome"]]
    trainedX, testedX, trainedY, testedY = train_test_split(x, y, test_size=0.3)
    trainedX.shape
    trainedY.shape
    clf = MLPClassifier(hidden_layer_sizes=(51),solver="lbfgs",alpha=1e-5, activation="logistic")
    clf.fit(x, y)
    y_pred=clf.predict(trainedX)
    print(accuracy_score(trainedY, y_pred))
    return clf

