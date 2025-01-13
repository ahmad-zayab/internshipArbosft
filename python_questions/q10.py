def rePermute(index, s, ans):

 
    if index == len(s):
        ans.append("".join(s))
        return

    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        rePermute(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]


ans=[]
s='abc'      
ans=rePermute(0,list(s),ans)

print("output ",ans)