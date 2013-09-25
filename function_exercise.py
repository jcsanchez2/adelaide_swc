import sys
def dnastats(filename):
    data = open (filename,'r')
    line = data.readline()
    seqcount = 0
    while line !='':
        line = line.rstrip()
        if line.startswith('>'):
            print 'name is :' + line       
        else:
            line.upper()
            print line        
        line = data.readline()



print dnastats('dnas.fasta')
