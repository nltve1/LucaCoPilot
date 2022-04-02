
# Press the green button in the gutter to run the script.
import random

import requests as requests

if __name__ == '__main__':
    # What's your name?
    name = input("What's your name? ")
    print("Hello, {}!".format(name))

    # What's your age?
    age = input("What's your age? ")
    print("You're {} years old.".format(age))
    # How are you doing
    feeling = input("How are you doing? ")

    feelings = ["good", "fine", "great", "awesome", "amazing", "fantastic", "superb", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "fantabulous", "super", "wonderful", "excellent", "terrific", "pretty good", "super", "wonderful", "excellent", "terrific"]

    if feeling.lower() in feelings:
        print("I'm glad to hear that!")
    else:
        print("I'm sorry to hear that.")

    # Print my name is jake
    print("My name is Jake")

    print("My ages is also {}".format(age))

    # Wanna play a game?
    play = input("Wanna play a game? ")

    if play.lower() == "yes":
        # Rock Paper Scissors
        myGame = input("Rock, Paper, Scissors? ")
        if myGame.lower() == "rock":
            print("You chose rock")
            computerChoice = random.choice(["rock", "paper", "scissors"])
            print("I chose {}".format(computerChoice))
            if computerChoice == "rock":
                print("It's a tie!")
            elif computerChoice == "paper":
                print("You lose!")
            elif computerChoice == "scissors":
                print("You win!")
        elif myGame.lower() == "paper":
            print("You chose paper")
            computerChoice = random.choice(["rock", "paper", "scissors"])
            print("I chose {}".format(computerChoice))
            if computerChoice == "rock":
                print("You win!")
            elif computerChoice == "paper":
                print("It's a tie!")
            elif computerChoice == "scissors":
                print("You lose!")
        elif myGame.lower() == "scissors":
            print("You chose scissors")
            computerChoice = random.choice(["rock", "paper", "scissors"])
            print("I chose {}".format(computerChoice))
            if computerChoice == "rock":
                print("You lose!")
            elif computerChoice == "paper":
                print("You win!")
            elif computerChoice == "scissors":
                print("It's a tie!")
        else:
            print("That's not a valid choice")
    else:
        print("Okay, maybe later")

    # wanna play another game?
    playAgain = input("Wanna another game? ")
    if playAgain.lower() == "yes":
        print("Okay, let's play a guessing game!")
        # guess a number between 1 and 10
        secretNumber = random.randint(1, 10)
        print("I'm thinking of a number between 1 and 10")
        guess = int(input("What's your guess? "))
        if guess == secretNumber:
            print("You guessed it!")
        else:
            print("Sorry, you didn't guess it. The number was {}".format(secretNumber))
    else:
        print("Okay, maybe later")

        # whats your favorite game?
        favoriteGame = input("What's your favorite game? ")
        if favoriteGame.lower() == "rock paper scissors":
            print("I love rock paper scissors too!")
        else:
            print("I don't like {} my favorite game is rock paper scissors ".format(favoriteGame))

    # Read api for weather
    apiKey = "3ed26093ade079653c8e573e59b0a8a9"
    city = input("What city do you want the weather for? ")
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, apiKey)
    response = requests.get(url)
    responseJSON = response.json()

    print("{} degrees celcius".format(responseJSON["main"]["temp"]))

    # I have to go somewhere bye
    print("I have to go bye")



# See PyCharm help at httpLucas://www.jetbrains.com/help/pycharm/
