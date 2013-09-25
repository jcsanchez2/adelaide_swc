import sys

page = open('pg76.txt','r')
line = page.readline()
count=0
lines=0
while line != '':
    count +=len(line) 
    lines +=1
    line = page.readline()
page.close()

print 'Total lines: ',lines,'line count ',count
print 'total length: %d, line count: %d' %(lines,count)
