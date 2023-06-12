from random import shuffle

print("Welcome to my quiz about capital cities in Europe!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    print("Ok, bye!")
    quit()

print("Choose the difficulty level:")
level = input("Easy - press '1'\nMedium - press '2'\nHard - press '3'")

easy = {
    "poland": "warsaw",
    "england": "london",
    "france": "paris",
    "spain": "madrid",
    "germany": "berlin",
    "italy": "rome",
    "austria": "vienna",
}
medium = {
    "bulgaria": "sofia",
    "belarus": "minsk",
    "croatia": "zagreb",
    "finland": "helsinki",
    "greece": "athens",
    "norway": "oslo",
    "sweden": "stockholm",
}
hard = {
    "north macedonia": "skopje",
    "moldova": "chisinau",
    "malta": "valetta",
    "liechtenstein": "vaduz",
    "iceland": "reykjavik",
    "estonia": "tallinn",
    "albania": "tirana",
}

print("Ok, let's start!")
# questions = 5


def quiz(level):
    score = 0
    if level == '1':
        # countries = shuffle(easy)
        for country in easy:
            print("What is the capital city of", country, "? ")
            answer = input()
            if answer.lower() == easy[country]:
                print("Correct")
                score += 1
            else:
                print("Incorrect")
    elif level == '2':
        for country in medium:
            print("What is the capital city of", country, "? ")
            answer = input()
            if answer.lower() == medium[country]:
                print("Correct")
                score += 1
            else:
                print("Incorrect")
    elif level == '3':
        for country in hard:
            print("What is the capital city of", country, "? ")
            answer = input()
            if answer.lower() == hard[country]:
                print("Correct")
                score += 1
            else:
                print("Incorrect")
    result = (score/len(easy))*100
    if result >= 90:
        print("You're great! You've got " +
              str(result)+"%"+" answers correct!")
    elif 40 < result < 90:
        print("You're not so bad. You've got " +
              str(result)+"%"+" answers correct!")
    else:
        print("You need to practice! You've got only " +
              str(result)+"%"+" answers correct!")


quiz(level)


"""
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
"""
