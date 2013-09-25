import sys
page = open('/home/swc_trainee/bootcamp/loops/Pitching.csv','r')
line = page.readline()
line = page.readline()


line_count = 0
total_ipouts = 0

while line !='':
    row = line.split(',')
    value = row[12]
    total_ipouts += float(value)
    line_count += 1
    line = page.readline()

total_average = total_ipouts/line_count
print 'total ipouts: ' + str(total_ipouts)
print 'line count: ' + str(line_count)
print 'total average ' + str(total_average)
