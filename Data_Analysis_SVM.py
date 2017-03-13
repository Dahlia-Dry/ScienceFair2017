# Author Dahlia Dry
# Version 1.1
#Last Modified 12/7/16
#This program builds an optimized linear SVM model to classify data.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn import svm
X = []
y=[]
target = open('november_15_with_temp.csv', 'r')
data = pd.read_csv(target, sep=',', header = None, names = ['ADC_Value', 'Temperature'])
for i in range(0,17280):
    data['ADC_Value'][i] = float(data['ADC_Value'][i])
    data['Temperature'][i] = float(data['Temperature'][i])
    X.append([data['ADC_Value'][i], data['Temperature'][i]])
    if i == 0:
	    y.append(0)
    elif data['ADC_Value'][i-1] - data['ADC_Value'][i] > 0:
        y.append(0)
    else:
        y.append(1)
X = np.array(X)
y = np.array(y)
C=0
gamma=0
max_accuracy = 0
while C <= 10000 && gamma <= 10000:
    svm = svm.SVC(kernel=linear, C=C, gamma=gamma)
    svm.fit(X,y)
    accuracy = svm.score(X,y)
    if accuracy > max_accuracy:
        accuracy = max_accuracy
        best_c = C
        best_gamma = gamma
    C = C + 100
    gamma = gamma+100
optimal_svm = svm.svc(kernel=linear, C=best_c, gamma=best_gamma)
optimal_svm.fit(X,y)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
 np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
Z = optimal_svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('ADC Value')
plt.ylabel('Temperature')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with Linear kernel')
plt.show()