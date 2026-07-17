import random

def responses():
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    random_number = random.randint(1, 20)
    return answers[random_number - 1]

def main():
    ready = input("Are you ready to ask the Magic 8 Ball a question? (press enter to continue, or type 'quit' to exit): ")
    if ready.strip().lower() == "quit":
        print("Exiting.")
        return

    history = []

    while True:
        user_question = input("Ask away! (press enter to quit): ")
        if user_question == "":
            print("Exiting.")
            break
        answer = responses()
        print(answer)
        history.append((user_question, answer))

    print("\n--- Question history ---\n")
    for question, answer in history:
        print(f"Question asked: {question}")
        print(f"Answer given: {answer}\n")
        
if __name__ == "__main__":
    main()