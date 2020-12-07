import keyboard
import sys
import time
import winsound
import matplotlib.pyplot as plt
#интервал 5 секунд, 6 циклов

freq = 500
dur = 100

'''a = [1,2,3,4,5]
plt.plot(a)
plt.show()'''
array1 = []
array2 = []
array3 = []
array4 = []
array5 = []
array6 = []


timer_begin = time.time()

timez = 0
while time.time() - timer_begin < 30:
    winsound.Beep(freq, dur)
    record = keyboard.record()
    array1.append(record)
    time.sleep(1)
    if time.time() - timer_begin % 5 == 0:
        print(array1)
        winsound.Beep(freq, dur)
    timez += 1

    print(array1)

#print(array1)
timer_end = time.time()
print(timer_end, timer_begin)
timer_secs = timer_end - timer_begin
'''for key in array:
    count = frequency.get(key,0)
    frequency[key] = count + 1'''