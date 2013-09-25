import sys

list = sys.argv[1:]

list.sort()
list[0] = list[0].title()
comb=','.join(list[0:-1])

comb += ', and ' + list[-1] + '.'

print comb
