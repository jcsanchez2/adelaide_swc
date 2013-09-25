import sys
###Testing git branches
string = 'ATGACTGACCAATGACCACTA'

def test1(seq,prefix):
    return seq[0:len(prefix)] == prefix 

print test1(string)   






