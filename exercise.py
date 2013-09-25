import sys
list =sys.argv
list.remove(list[0])
list.sort()

a = ', and '
b = '.'
list[0] = list[0].title()
print list[0]
newlast= a+list[-1]+b
comb=','.join(list[0:-1])
final=comb+newlast



print final
#print 'hello world'

