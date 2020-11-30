import numpy as np
import random
import matplotlib.pyplot as plt
'''a = np.array([20,30,40,50])
b = np.arange(4)
print('a=', a)
print('b=', b)
print(10*np.sin(a))
for i in a:
    print(i**(12**2))'''



'''a = np.array([i**2 for i in range(100)])
plt.plot(a)
print(a)
plt.show()'''

a = np.array([[random.randint(1,100) for i in range(10)] for z in range(10)])
print(a)
b = np.diagonal(a)
plt.plot(b)
plt.show()

'''a = np.array([[random.randint(1,10) for i in range(2)] for z in range(2)])
b = np.array([[random.randint(1,10) for i in range(2)] for z in range(2)])
a @ b
print(a @ b)

'''
