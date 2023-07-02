prime_list=[]

for i in range(0,1000):
    if i==0 or i==1:
        continue
    else:
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            prime_list.append(i)
if len(prime_list)==0:
    print("There is no any prime numbers in between 0 to 999")
else:
    print("Prime numbers between 0 to 999 are-",prime_list,end="  ") 
