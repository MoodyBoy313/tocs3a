# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17mIAoISCoz-j70k6TlhOGbzYoNsQ_ruW
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
data = '/content/car_evaluation.csv'
df = pd.read_csv(data, header=None)
df.shape
df.head()
col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot',
'safety', 'class']
df.columns = col_names
col_names
df.info()
df['class'].value_counts()
df.isnull().sum()
X = df.drop(['class'], axis=1)
y = df['class']
# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =
0.33, random_state = 42)
# check the shape of X_train and X_test
X_train.shape, X_test.shape
X_train.dtypes
X_train.head()
X_test.head()

from sklearn.tree import DecisionTreeClassifier
# instantiate the DecisionTreeClassifier model with criterion gini index

clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3,
random_state=0)
# fit the model
clf_gini.fit(X_train, y_train)

y_pred_gini = clf_gini.predict(X_test)

from sklearn.metrics import accuracy_score
print('Model accuracy score with criterion gini index: {0:0.4f}'.
format(accuracy_score(y_test, y_pred_gini)))


y_pred_train_gini = clf_gini.predict(X_train)
y_pred_train_gini

print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train,
y_pred_train_gini)))


print('Training set score: {:.4f}'.format(clf_gini.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(clf_gini.score(X_test, y_test)))


plt.figure(figsize=(12,8))
from sklearn import tree
tree.plot_tree(clf_gini.fit(X_train, y_train))

import graphviz
dot_data = tree.export_graphviz(clf_gini, out_file=None,
 feature_names=X_train.columns,
 class_names=y_train,
 filled=True, rounded=True,
 special_characters=True)
graph = graphviz.Source(dot_data)
graph