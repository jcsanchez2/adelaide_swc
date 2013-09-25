#gc content
#base count
#reverse complement

class NucleotideString:
    base_comp = { 'A':'T','T':'A','G':'C','C':'G'}

    
    def __init__(self,seq):
        self.seq=seq        
        self.bases = {}

    def gc_content(self):
        GCs = self.seq.count('G') + self.seq.count('C')
        return float(GCs) / len(self.seq)  


    def base_count(self,base):
        if base in self.bases:
            return self.bases[base]
        else:
            self.bases[base] = self.seq.count(base)
            return self.bases revcomp(self):
        compl = ''
        for base in self.seq:
            compl = self.base_comp[base] + compl
        return compl


class DNAString(NucleotideString):
    pass
class RNAString(NucleotideString):
        base_comp = { 'A':'U','U':'A','G':'C','C':'G'}
    



