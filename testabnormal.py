from random import randint
try:
    open('abc.txt','r')
    print(aa)
except BaseException as msg:
    print(msg)

number = randint(1,9)
if number %2 == 0:
    raise NameError("%d is even" % number)
else:
    raise NameError("%d is odd" % number)