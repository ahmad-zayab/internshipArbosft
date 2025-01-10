

def longest_unique_substring(s: str):
    s1=s[0]
    s2=s[1]
    list1=[]
    count=0
    j=1
    maxcount=0
    index=0

    for i in range(len(s)):

        for j in range(len(s)):

            if s[i]!=s[j]:
                count+=1

            else:
                if count>=maxcount:
                    maxcount=count
                    index=i

                count=0
    return index,maxcount
                






       

    


s=input("Enter Strring \n")        
index,maxcount=longest_unique_substring(s)
print("longest substring ",index,maxcount)

