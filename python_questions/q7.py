def reverse_words(sentence: str):
    word=' '
    sent=' '

    for i in range(len(sentence)):
        
        ch=sentence[i]

        if ch!=' ':
            word+=ch
        else:
            word=word[::-1]  
            print(word)
            sent+=word
            sent+=' '
            word=' '
        if i==len(sentence)-1:
            word=word[::-1]  
            print(word)
            sent+=word
            

  
      
    return sent


s=input("Enter Sentence \n")        
n=reverse_words(s)
print("Sentence is reversed",n)