s="ahmahamhcma"
p="mah"
n=len(p)
l=[]
def find_all_anagrams(s: str, p: str):
   
    for i in range(len(s)): 
    
        if(sorted(s[0:n])== sorted(p)):
            l.append(i+1)
        
        s=s[1:]
        if len(s)==1:
            break

    return l    


   

find_all_anagrams(s,p)
print(l)

