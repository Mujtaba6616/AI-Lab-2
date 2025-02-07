
import seaborn



import matplotlib as plt

from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = np.array(iris.data)
Y = np.array(iris.target)

m=np.mean(X)
print(m)

med=np.median(X)
print(med)

std= np.std(X)
print(std)


m=np.mean(Y)
print(m)

med=np.median(Y)
print(med)

std= np.std(Y)
print(std)


min=np.min(X)
max=np.max(X)
print(min, max)

min=np.min(Y)
max=np.max(Y)
print(min, max)


sepal_length= X[:,0]
sepal_width=X[:,1]
petak_length= X[:,2]
petal_width=X[:,3]
print("Sepal Length Mean:", np.mean(sepal_length),
      ", Median:", np.median(sepal_length),
      ", Std Dev:", np.std(sepal_length),
      ", Min:", np.min(sepal_length),
      ", Max:", np.max(sepal_length))

print("Sepal Width -> Mean:", np.mean(sepal_width),
      ", Median:", np.median(sepal_width),
      ", Std Dev:", np.std(sepal_width),
      ", Min:", np.min(sepal_width),
      ", Max:", np.max(sepal_width))



plt.scatter(sepal_length, sepal_width)

plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()




plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.show()



plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

