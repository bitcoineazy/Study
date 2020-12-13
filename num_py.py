import numpy as np
import random
import matplotlib.pyplot as plt
import math
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

#a = np.array([[random.randint(1,100) for i in range(10)] for z in range(10)])
b = np.array([[random.randint(1,19) for i in range(10)] for z in range(10)])

sin = np.array([math.sin(i) for i in range(10)])
cos = np.array([math.cos(i) for i in range(10)])
#p = np.reshape(b, 100)
#print(a)
#z = np.diagonal(b)
#print(p)
plt.axis([0,10,-1,1])
plt.plot(sin)
plt.plot(cos)
plt.show()

'''a = np.array([[random.randint(1,10) for i in range(2)] for z in range(2)])
b = np.array([[random.randint(1,10) for i in range(2)] for z in range(2)])
a @ b
print(a @ b)

'''
