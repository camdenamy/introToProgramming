time_of_day = input("What time of day is it?: ")
age = int(input("What is your age?: "))

if age < 4:
    price = 0
    print("free")
    
else:
    if time_of_day in('night'):
        if age >= 55:
            price = 13
            print(f"${price}")
        if (age >= 17) and (age <= 54):
            price = 15
            print(f"${price}")
        if (age >= 4) and (age <= 16):
            price = 12
            print(f"${price}")
        
    elif time_of_day in('day'):
        price = 8
        print(f"${price}")