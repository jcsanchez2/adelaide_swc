input_string = 'A very, very long sentence.'
input_string = input_string.lower()
myset = set(input_string)
##also have to remove non Aa-Zz characters, several ways to do it
length = len(myset)

print myset
print length
