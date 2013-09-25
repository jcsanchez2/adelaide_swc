import sys
string = 'ATGACTGNATACCTAGGAACATACNNTGACTAATAG'
def dnafun(seq):
    seq = seq.replace('N','')    
    Gs = seq.count('G')
    Cs = seq.count('C')
    return float((Gs + Cs)) / len(seq)

print dnafun(string)
