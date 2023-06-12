print("Welcome to my quiz about capital cities in Europe!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    print("Ok, bye!")
    quit()

print("Ok, let's start!")
score = 0
questions = 5

answer = input("What is the capital city of Poland? ")
if answer.lower() == "warsaw":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of England? ")
if answer.lower() == "london":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of France? ")
if answer.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of Italy? ")
if answer.lower() == "rome":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the capital city of Norway? ")
if answer.lower() == "oslo":
    print("Correct")
    score += 1
else:
    print("Incorrect")

result = (score/questions)*100

if result >= 90:
    print("You're great! You've got " +
          str(result)+"%"+" answers correct!")
elif 40 < result < 90:
    print("You're not so bad. You've got " +
          str(result)+"%"+" answers correct!")
else:
    print("You need to practice! You've got only " +
          str(result)+"%"+" answers correct!")
