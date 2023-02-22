# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if len(str(year)) !=4:
    print("give four digit number")
else:
    if (year %4)!=0:
         print("not leap year")
    else:
        if (year%100)!=0:
            print(" Leap year")
        else:
            if (year%400)!=0:
                print("not leap year")
            else:
                print("Leap year")   




