num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 == num3:
    print(f"Max of {num1} and {num2} and {num3} is {num1}")

if not(num1 == num2 == num3):
    if num1 > num2:
        max = num1
    if num2 > num1:
        max = num2
    if num3 > max:
        max = num3

    print(f"Max of [{num1}, {num2}, {num3}] is {max}")