import json

jsonDumpsIndentStr = json.dumps(demoDictList, indent=1);
print "jsonDumpsIndentStr=",jsonDumpsIndentStr;

try:
    open('abc.txt','r')
    print(aa)
except BaseException as msg:
    print(msg)