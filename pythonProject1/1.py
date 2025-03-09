import time

for i in range (1000):
    print('\r{}%'.format(i),end=" ")
    time.sleep(0.1)