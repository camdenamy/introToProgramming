# Prompt user asking if they are ready to take the quiz
ready_or_not = input("Are you ready to take the quiz?: ").lower()
# If input is anything other than a word that starts with the letter n or "no" then continue
if not ready_or_not.startswith('n'):
    # initialize score with 0
    total_score = 0
    
    # List 1st question and responses
    print("Is Die Hard a Christmas movie?: \n" "A. Yes!\n" "B. No\n" "C. (A) but with 2 !!\n" "D. A and C\n")
    question1 = input("Your answer: ").lower()
    # If correct, inform user and increse score by 1
    if question1 in ('a', 'c', 'd'):
        print("Correct!\n")
        total_score += 1
    # If incorrect, do not increase score
    else:
        print("Incorrect\n")
        
    # List 2nd question and responses
    print("Does the Dude abide?:\n" "A. Yes\n" "B. No\n" "C. I'm not Lebowski\n" "D. Who is the Dude?!\n")
    question2 = input("Your answer: ").lower()
    # If correct increase score by 1
    if question2 == 'a':
        print("Correct!\n")
        total_score += 1
    # If incorrect, do not increase score
    elif question2 == 'c':
        print("Incorrect, but you have great taste in movies!\n")
    elif question2 == 'd':
        print("You have homework. Watch The Big Lebowski!\n")
    else:
        print("Incorrect\n")
        
    # List 3rd question and responses
    print("What is the flight speed of a laden swallow?:\n" "A. 10 m/s\n" "B. African or European?\n" "C. 25 m/s\n" "D. 5 m/s\n")
    question3 = input("Your answer: ").lower()
    # If correct increase score by 1
    if question3 == 'b':
        print("Correct! You may continue on your quest for the Holy Grail.\n")
        total_score += 1    
    # If incorrect do not increase score
    else:
        print("Incorrect\n")
        
    # List 4th question and responses
    print("Which Fast & Furious movie almost ended the franchise?:\n" "A. Everything after the 4th one\n" "B. Tokyo Drift\n" "C. Fast & Furious 2\n" "D. Every movie after The Rock joined\n")
    question4 = input("Your answer: ").lower()
    # If correct increase score by 1
    if question4 == 'b':
        print("Correct!\n")
        total_score += 1
        # If incorrect do not increase score
    else:
        print("While those movies were really bad, B is the correct answer\n")
        
    # List 5th question and responses
    print("What movie is one of the best movies about games ever made?:\n" "A. Gamer\n" "B. Jumanji\n" "C. Ready Player One\n" "D. Halo: Fall of Reach\n")
    question5 = input("Your answer: ").lower()
    # If correct increase score by 1
    if question5 == 'c':
        print("Correct!\n")
        total_score += 1
    # If incorrect do not increase score
    else:
        print("Incorrect\n")
            
    # Print quiz complete and display total score out of 5 and then percentage correct
    while True:
        response = input("Press Enter to display score:\n")
        if response == "":
            print(f"Total score is {total_score} points\n")
            break
            
# If no then exit
else:
    print("Goodbye!")