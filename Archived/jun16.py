# for a in range(start, stop, step): start + step = stop - 1

# start = int(input("What number do you wnat to start with? "))
# howmany = int(input("How many numbers do you want to print after the first one? "))
# stop = 2*howmany + start
# for i in range(start, stop, 2):
#     print (i)
import time
for minute in range(1):
    for second in range(60):
        print(str(minute) + ":" + str(second))
        time.sleep(1)
        
