import time


files = open("pome.txt",'r')
strs = files.readlines()

try:
    for l in strs:
        print(l)
        time.sleep(1)
finally:
    files.close()
    print('Cleaning up ...closed the file')