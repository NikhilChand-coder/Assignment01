def adult_female(bmi):
    if bmi>=17.8 and bmi<26.5:
        print("You are Normal.")
        print("BMI=",r_bmi,"kg/m^2")
    elif bmi<17.8:
        print("You are underweighted.")
        print("BMI=",r_bmi,"kg/m^2")
    else:
        print("You are overweighted.")
        print("BMI=",r_bmi,"kg/m^2")
    
def teenage_female(bmi):
    if bmi>=16.3 and bmi<24:
        print("You are Normal.")
        print("BMI=",r_bmi,"kg/m^2")
    elif bmi<16.3:
        print("You are underweighted.")
        print("BMI=",r_bmi,"kg/m^2")
    else:
        print("You are overweighted.")
        print("BMI=",r_bmi,"kg/m^2")



def adult_male(bmi):
    if bmi>=18.5 and bmi<25:
        print("You are Normal.")
        print("BMI=",r_bmi,"kg/m^2")
    elif bmi<18.5:
        print("You are underweighted.")
        print("BMI=",r_bmi,"kg/m^2")
    else:
        print("You are overweighted.")
        print("BMI=",r_bmi,"kg/m^2")
    
def teenage_male(bmi):
    if bmi>=18.7 and bmi<26.3:
        print("You are Normal.")
        print("BMI=",r_bmi,"kg/m^2")
    elif bmi<18.7:
        print("You are underweighted.")
        print("BMI=",r_bmi,"kg/m^2")
    else:
        print("You are overweighted.")
        print("BMI=",r_bmi,"kg/m^2")

        


gender=int(input("1=Male  2=Female : "))
age=int(input("Enter your age (b/w 2 to 120): "))
height=int(input("Enter your height (in cm.) : "))
weight=int(input("Enter your weight (in kg.) : "))
height_meter=height/100
bmi=(weight/(height_meter**2))
r_bmi=format(bmi,".2f")


if gender==1:
    if age>2 and age<=20:
        teenage_male(bmi)
    elif age>21 and age<120:
        adult_male(bmi)
        
elif gender==2:
    if age>2 and age<=20:
        teenage_female(bmi)
    elif age>21 and age<120:
        adult_female(bmi)
else:
    print("Invalid Entered")
