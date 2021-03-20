from sklearn import datasets, svm, utils
import random

digits = datasets.load_digits()

digits.target, digits.data = utils.shuffle(digits.target, digits.data)

two_third = int(len(digits.data)/3*2)  #Selects only 2/3 of the data

clf = svm.SVC(gamma=0.001, C=100)
X, y = digits.data[:-two_third], digits.target[:-two_third]
clf.fit(X, y)

amount_wrong = 0
for x in range(len(digits.data)-two_third):
    target = -random.randint(1, len(digits.data)-two_third)

    predict = clf.predict(digits.data[target:target+1])
    answer = digits.target[target:target+1]
    if predict != answer:
        amount_wrong += 1

print(amount_wrong, "out of", len(digits.data)-two_third, "wrong")
print("Percentage correct:", 100-round((amount_wrong / (len(digits.data)-two_third)) * 100), "%")
