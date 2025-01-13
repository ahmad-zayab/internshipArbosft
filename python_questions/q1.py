s= input("Enter string \n")
longest = ""
n1 = n2 = 0
s1 = s2 = ""
for i in range(len(s)): 
   
    if s==s[::-1]:
        n1=len(s)
        s1=s

        break
       
    s=s[1:]
    if len(s)==1:
        break

s0=s[::-1]
for i in range(len(s0)): 
   
    if s0==s0[::-1]:
        n2=len(s0)
        s2=s0
        break
       
    s0=s0[1:]
    if len(s0)==1:
        break
    
if n1>=n2:
    print(s1)

else:
    print(s2)