score = 0   

  

#question#1 

print( 

    "Question: I am one of the following:\n" 

    "1. A U.S. citizen and resident of California.\n" 

    " OR \n" 

    "2. A U.S. citizen and a member of the Uniformed Services or Merchant Marine on active duty outside my county.\n" 

    "3. A U.S. citizen and an eligible spouse or dependent of a member of the Uniformed Services or Merchant Marine on active duty outside my county.\n" 

    "4. A U.S. citizen and an activated National Guard member on State orders outside my county.\n" 

    "5. A U.S. citizen residing outside the U.S. temporarily.\n" 

    "6. A U.S. citizen residing outside the U.S. indefinitely.\n" 

    "7. A U.S. citizen and have never resided in the U.S.\n") 

  

Question1 = input("Your Answer: ") 

  

if Question1 in ["1", "2", "3", "4", "5", "6", "7", "8"]:  

    score += 1 

else: 

    score-= 1  

     
# Question 2 

print( 

    "Question:I am 18 years or older? \n" 

    "YES\n" 

    "NO\n" ) 

  

Question2 = input("Your Answer: ") 

  

if Question2.upper() == "YES": 

    score += 1 

else: 

    score -= 1 

     

     

# Question 3 

print( 

    "Question: Are you serving a state or federal prison term?:\n" 

    "YES\n" 

    "NO\n") 

  

Question3 = input("Your Answer: ") 

  

if Question3.upper() == "NO": 

    score += 1 

else: 

    score -= 1 


print("Your score:", score,"/3") 

print("If you got less than 3 you are not eligible to vote.")

