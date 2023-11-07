# ----MODULES----
import random, time

# ----VARIABLES----
response = False
name = ""
answers_list = [
    {"id": 1, "answer": "Yes - definitely"},
    {"id": 2, "answer": "It is decidedly so"},
    {"id": 3, "answer": "Without a doubt"},
    {"id": 4, "answer": "Reply hazy, try again"},
    {"id": 5, "answer": "Ask again later"},
    {"id": 6, "answer": "Better not tell you now"},
    {"id": 7, "answer": "My sources say no"},
    {"id": 8, "answer": "Outlook not so good"},
    {"id": 9, "answer": "Very doubtful"},
]


# ----FUNCTIONS----
def welcome(name):
    print(
        """
----------------Welcome to the Magic 8 Ball game!----------------
                        ____
                     ,dP9CGG88@b,
                   ,IP  _   Y888@@b,
                  dIi  (_)   G8888@b
                 dCII  (_)   G8888@@b
                 GCCIi     ,GG8888@@@
                 GGCCCCCCCGGG88888@@@
                 GGGGCCCGGGG88888@@@@...
                 Y8GGGGGG8888888@@@@P.....
                  Y88888888888@@@@@P......
                  `Y8888888@@@@@@@P'......
                     `@@@@@@@@@P'.......
                         ''''........

Handy Notes:
  - At any point if you answer with 'q' it will quit the game
  - Yes OR No questions only, otherwise be disappointed :/ 

----------------------------------------------------------------
    """
    )
    name = input("Whats your name? ") or "User"
    return name


def goodbye(name):
    if name.lower() == "q":
        print("\nThanks for playing, User!\n")
    else:
        print(f"\nThanks for playing, {name}!\n")
    print("----------------------------------------------------------------\n")
    time.sleep(2)


def ask_user(name):
    if name.lower() == "q":
        goodbye(name)
        return True
    question = input("\nAsk a yes or no question: ") or "Nothing"
    if question.lower() == "q":
        goodbye(name)
        return True
    evaluation = name == "User" and question == "Nothing"
    final_question = None
    if evaluation:
        print(
            "You need to fill in your name and ask a question before the Magic8 Ball answers!\n"
        )
        return False
    elif name == "User":
        print("You need to fill in your name before the Magic8 Ball answers!\n")
        return False
    elif question == "Nothing":
        print("You need to ask a question before the Magic8 Ball answers!\n")
        return False
    else:
        answer = random.choice(answers_list)
        # print(f"\n>> {name}'s asks: '{question}' **while shaking the Magic8 ball..**")
        print(f"\n>> MAGIC 8 BALL'S ANSWER: {answer['answer']}\n")
        print("----------------------------------------------------------------\n")
        final_question = input(
            "Shake the Magic8 ball and ask another question? (Y or N)? "
        )
        if final_question.lower() == "y":
            return False
        else:
            goodbye(name)
            return True


# ----OUTPUT----
name = welcome(name)
while not response:
    response = ask_user(name)
