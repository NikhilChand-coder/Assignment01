n=int(input("Enter the Number: "))
print("Table by For loop")
for i in range(1,11):
    print(n,"*",i,"=",n*i)


print("Table by While loop")
j=1
while j<=10:
    print(n,"*",j,"=",n*j)
    j+=1
else:
    print("Code Successfully Executed")
