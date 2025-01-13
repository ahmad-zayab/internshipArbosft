def first_unique_char(s: str):
    
    for i in range(len(s)):
        found=False
        for j in range(len(s)):
            if i!=j and s[i]==s[j]:
                found=True
                break
        if not found:
            return i

            

s=input("Enter String \n")        
n=first_unique_char(s)
print("Index is ",n)




                