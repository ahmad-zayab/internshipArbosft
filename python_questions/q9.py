def evaluate_expression(expr: str):
    ls=[]
    s1=[]
    ans=0
    for i in range(len(s)):
        if s[i].isdigit() or s[i]=='+' or s[i]=='-':
            ls.append(s[i])
        
    for i in range(len(s)):
        if ls[i].isdigit():
            s1.push(ls[i])
        elif ls[i]=='+'or ls[i]=='-':
            x=s1.pop()
            ans=ans+x+ls[i]



        


    return ls





s=input("Enter Strring \n")        
i=evaluate_expression(s)
print("output ",i)