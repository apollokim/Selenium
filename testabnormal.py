try:
    open('abc.txt','r')
    print(aa)
except BaseException as msg:
    print(msg)