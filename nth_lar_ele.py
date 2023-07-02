list=[]
n=int(input("Enter the number of items in list: "))


for i in range(0,n):
    items=int(input("Enter number:"))
    list.append(items)

    
nth=int(input("Which largest term do you want to print: "))


list.sort(reverse=True)

if nth>n:
    print("This term is not present in the list")
else:
    if nth==1:
        print(nth,"st largest number in the list is ",list[nth-1])
    elif nth==2:
        print(nth,"nd largest number in the list is ",list[nth-1])
    elif nth==3:
        print(nth,"rd largest number in the list is ",list[nth-1])
    else:
        print(nth,"th largest number in the list is ",list[nth-1])
