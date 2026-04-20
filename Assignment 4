import numpy as np
import matplotlib.pyplot as plt

#1a
numbers = [3, 1, 5, 12, 15, 90, 2, 6, 10, 11]
nums = np.array(numbers).reshape(5, 2)

#1b
numbers2 = [2,5,3,7,10,6,8,1,0,4,9,11]
C = np.array(numbers2).reshape(3, 4)
print("\n",C[1])
print("\n",C[:, 3])
#There is no row 4 so I printed rows 2 and 3
print("\n",C[1:3])

C = np.insert(C, 0, 1, axis = 1)
print("\n",C)

print("\n",C[2, 1])

#1c
A = np.array(numbers2).reshape(6,2)
B = np.array([3,1,2,5,4,9]).reshape(3,2)
#Inner dimensions don't match, cannot do dot product
#print("\n",np.dot(A, B))

#2a
A1 = np.array(numbers2).reshape(12, 1)
A1 = np.insert(A1, 0, 1, axis=1)
b = np.array([2,7,1,5,3,1,2,3,3,1,4,2]).reshape(12,1)
x = np.linalg.lstsq(A1, b)[0]
print("Intercept: ", x[0,0])
print("Slope: ", x[1,0])

#2b
rng = np.random.default_rng()
random = rng.random((3,4))
print("Total sum: ", np.sum(random))
print("Row sums: ", np.sum(random, axis = 1))
print("Column sums: ", np.sum(random, axis = 0))
print("Column means: ", np.mean(random, axis = 0))
print("Row standard deviation ", np.std(random, axis = 1))

#2c
data = rng.normal(loc = 0, scale = 2.5, size = 100)
plt.hist(data, bins = 15, edgecolor = "black")
plt.title("Histogram of normally distributed data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

