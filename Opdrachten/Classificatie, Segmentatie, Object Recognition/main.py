import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import random

digits = datasets.load_digits()
two_third = int(len(digits.data)/3*2)  #Selects only 2/3 of the data

clf = svm.SVC(gamma=0.001, C=100)
X, y = digits.data[:-two_third], digits.target[:-two_third]
clf.fit(X, y)

random.shuffle(digits.data)

for x in range(30):
    target = -random.randint(1, len(digits.data)-two_third)
    print("predict:", clf.predict(digits.data[target:target+1]))
    plt.imshow(digits.images[target], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()

"Van de 30 runs was er 1 fout, dus een accuracy van 96.67%"
