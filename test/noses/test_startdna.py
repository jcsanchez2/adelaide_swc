
class UnknownBaseException(Exception):
    pass


def dnastart(seq,prefix):
    if 'N' in seq:
        raise UnknownBaseException()    
    return seq[0:len(prefix)] == prefix 

def test_first():
    assert dnastart('atgact','at')

def test_start_itself():
    dna= 'ACTGATG'
    assert dnastart(dna,dna)


