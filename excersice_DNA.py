input_string = 'ATGACCTGACTACCCAATTGACTACCATGGATTACCTAAGTAC'

na = input_string.count('A') 
nc = input_string.count('C') 
nt = input_string.count('T') 
ng = input_string.count('G') 

counts = {'A':na,'G':ng,'T':nt,'C':nc}
print counts

print float(counts['G'] + counts['C']) / len(input_string)

from collections import Counter
##dictionary with nt occurences
print Counter(input_string)



