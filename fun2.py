    
def change_list(a_list):
    a_list[0] = 'changed'

a=[1,2,3,4]
change_list(list(a))
print a
