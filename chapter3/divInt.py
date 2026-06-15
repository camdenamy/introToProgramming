user_num = int(input())
div_num = int(input())

left_over1 = user_num // div_num
left_over2 = left_over1 // div_num
left_over3 = left_over2 // div_num

print(left_over1,left_over2,left_over3)