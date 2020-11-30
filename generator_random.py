import datetime
import numpy as np
import matplotlib.pyplot as plt
import random
import time

random = datetime.datetime.utcnow()
print(random.microsecond)
new = []


a = np.array([[random.microsecond for i in range(2)]for z in range(2)])
true = True
while true:
    time.sleep(0.1)
    for item in a:
        new.append(time.ctime())
    time.sleep(0.1)

print(new)
plt.plot(a)
plt.show()