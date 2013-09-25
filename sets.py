#given a string (sentence) find how many unique
#letter A-Z it contains - capital and lower cases shouldnt
#be double counted
import sys
mylist= sys.argv[1:]
var = ' '.join(mylist)
x = var.lower()
myset = set(x)
l = len(myset)

print l

