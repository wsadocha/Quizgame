from random import shuffle

print("Welcome to my quiz about capital cities in Europe!")

playing = input("Do you want to play? (y/n) ")

while playing.lower() == "y":

    print("Ok, let's start!")
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

    def quiz(level):
        score = 0
        if level == '1':
            c = list(easy.items())
            shuffle(c)
            countries = dict(c)

            # a way to limit the number of elements in the dictionary
            while len(countries) > 5:
                countries.popitem()

            for country in countries:
                print("What is the capital city of", country, "? ")
                answer = input()
                if answer.lower() == countries[country]:
                    print("Correct")
                    score += 1
                else:
                    print("Incorrect")
        elif level == '2':

            c = list(medium.items())
            shuffle(c)
            countries = dict(c)

            while len(countries) > 5:
                countries.popitem()

            for country in countries:
                print("What is the capital city of", country, "? ")
                answer = input()
                if answer.lower() == countries[country]:
                    print("Correct")
                    score += 1
                else:
                    print("Incorrect")
        elif level == '3':

            c = list(hard.items())
            shuffle(c)
            countries = dict(c)

            while len(countries) > 5:
                countries.popitem()

            for country in countries:
                print("What is the capital city of", country, "? ")
                answer = input()
                if answer.lower() == countries[country]:
                    print("Correct")
                    score += 1
                else:
                    print("Incorrect")
        result = (score/len(countries))*100
        if result >= 80:
            print("You're great! You've got " +
                  str(result)+"%"+" answers correct!")
        elif 40 < result < 80:
            print("You're not so bad. You've got " +
                  str(result)+"%"+" answers correct!")
        else:
            print("You need to practice! You've got only " +
                  str(result)+"%"+" answers correct!")

    quiz(level)
    playing = input("Do you want to play again? (y/n) ")

print("Ok, bye")
