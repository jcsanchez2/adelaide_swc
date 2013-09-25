import sys
list =sys.argv
list.remove(list[0])
list.sort()
list[0].upper()
a = ', and '
b = '.'
newlast= a+list[-1]+b
comb=','.join(list[0:-1])
final=comb+newlast



print final
#print 'hello world'

