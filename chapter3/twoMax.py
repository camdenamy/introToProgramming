num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 == num2:
    print(f"Max of {num1} and {num2} is {num1}")

if not(num1 == num2):
    if num1 > num2:
        max = num1
    
    if num2 > num1:
        max = num2

    print(f"Max of {num1} and {num2} is {max}")