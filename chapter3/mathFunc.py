import math

x = float(input())
y = float(input())
z = float(input())

value_1 = pow(x,z)
value_2 = pow(x,pow(y,z))
value_3 = abs(x - y)
value_4 = math.sqrt(pow(x,z))

print(f"{value_1:.2f} {value_2:.2f} {value_3:.2f} {value_4:.2f}")