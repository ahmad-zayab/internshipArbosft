


def compress_string1(s: str):
    l1=[]
    i=0
    output_str = s[0]
    count=0
    alpha = s[0]
    while i < len(s):
        if alpha != s[i]:
            output_str += str(count)
            alpha =s[i]
            output_str += str(alpha)
            count = 1
        else:
            count += 1
        i += 1
    if count>0:
        output_str += str(count)
    return output_str

def compress_string(s: str):
    l1=[]
    temp=''
    count=1
    flag=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            flag=1
            temp=s[i]
            count+=1
            continue
        else:
            if flag==0:
                temp=s[i]
            l1.append(temp)
            l1.append(count) 
            flag=0
            count=1  

    return l1
s=input("enter the string \n")
list1=compress_string1(s)
print(list1)
            




