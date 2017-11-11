from threading import *
import time

def lift_off(number):
    for i in range(10,0):
        print("#"+ i + "("+ number+ ")")

for x in range(3):
    Thread(target=lift_off, args=(x,)).start()

time.sleep(10)
