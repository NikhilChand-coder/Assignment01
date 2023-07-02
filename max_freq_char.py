str=input("Enter the string: ")
str_freq={}

for i in str:
    if i in str_freq:
        str_freq[i]+=1
    else:
        str_freq[i]=1
        
max_freq=max(str_freq,key=str_freq.get)

print("Character",max_freq,"has maximum frequency")
