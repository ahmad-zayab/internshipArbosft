s1="abcd"
s2="bca"
temp=''

def are_rotations(s1: str, s2: str):
    temp=s1+s1
    if temp.find(s2)>0:
        return 1
    else:
        return 0
    
 
if are_rotations(s1,s2):
    print("Yes")
else:
    print("No")