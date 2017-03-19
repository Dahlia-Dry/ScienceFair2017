import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn import svm
import random
X = []
y=[]
target = open('testsvmdata.csv', 'r')
data = pd.read_csv(target, sep=',', header = None, names = ['ADC_Value', 'Wind_Speed'])
for i in range(0,15000):
    data['ADC_Value'][i] = float(data['ADC_Value'][i])
    data['Wind_Speed'][i] = float(data['Wind_Speed'][i])
    noise = 3 * random.random()
    plusminus = random.randint(0,1)
    if plusminus == 0:
    	data['Wind_Speed'] -= noise
    elif plusminus == 1:
    	data['Wind_Speed'] += noise
    X.append([data['ADC_Value'][i], data['Wind_Speed'][i]])
    if i == 0:
	    y.append(0)
    elif data['ADC_Value'][i-1] - data['ADC_Value'][i] > 0:
        y.append(0)
    else:
        y.append(1)
X = np.array(X)
y = np.array(y)
clf = svm.SVC(kernel = 'linear', C=1, gamma=1000)
clf.fit(X,y)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
 np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Wind Direction (ADC Value)')
plt.ylabel('Temperature (C)')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with Linear kernel')
plt.show()