import sys

def ntContent(seq):
    dnaDict ={}
    uniques = set(seq)
    for nucleotide in uniques:
        dnaDict[nucleotide] = seq.count(nucleotide)
    return dnaDict

print ntContent('ATGAAAAT')





passes = 0    
for (i, (seq, expected)) in enumerate(Tests):    
  if nucleotideContent(seq) == expected:    
    passes += 1    
else:    
  print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(Tests)))
test = [
    ['gtcagtc', {'G':2, 'T':2, 'C':2, 'A':2}],
    ['ACTGHR', {}],
    ['gtagt', {'G':2, 'T':2, 'C':0, 'A':2}]]
