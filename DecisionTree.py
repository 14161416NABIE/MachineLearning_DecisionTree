# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZjFzbg67eB3NU17mFzhc5RnxbEDOSLMK
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

my_data=pd.read_csv('/content/drug200.csv')
print(my_data.tail(5))

x=my_data[['Age', 'Sex','BP','Cholesterol', 'Na_to_K']].values
print('x:', x)

y=my_data[['Drug']]
print('y:',y)

from sklearn import preprocessing
le_sex=preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
x[:,1]=le_sex.transform(x[:,1])
print(x[:,1])

le_BP=preprocessing.LabelEncoder()
le_BP.fit(['LOW','HIGH','NORMAL'])
x[:,2]=le_BP.transform(x[:,2])
print(x[:,2])

le_chol=preprocessing.LabelEncoder()
le_chol.fit(['HIGH','NORMAL'])
x[:,3]=le_chol.transform(x[:,3])
print(x[:,3])
print(x[0:5])

from sklearn.model_selection import train_test_split
x_trainset,x_testset,y_trainset,y_testset=train_test_split(x,y,test_size=0.3,random_state=3)

pip install "pandas<0.25.0"

#Modeling

from sklearn.tree import DecisionTreeClassifier

drugTree=DecisionTreeClassifier(criterion='entropy',max_depth=4)

drugTree.fit(x_trainset,y_trainset)

#prediction

predTree=drugTree.predict(x_testset)
print('Predic:',predTree[0:5])
print(y_testset[0:5])

#evaluation

from sklearn import metrics
print('DecisionTree Accuracy:', metrics.accuracy_score(y_testset,predTree))

from io import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree
dot_data=StringIO()
filename="drugTree.png"
featureNames=my_data.columns[0:5]
out=tree.export_graphviz(drugTree,feature_names=featureNames,out_file=dot_data,class_names=np.unique(y_trainset),filled=True,special_characters=True,rotate=False)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png(filename)
img=mpimg.imread(filename)
plt.figure(figsize=(100,200))
plt.imshow(img,interpolation='nearest')