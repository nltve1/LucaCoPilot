import random
import requests

# Global Variables
cnt = 1


def getWeather(city):
    # Read api for weather
    apiKey = "3ed26093ade079653c8e573e59b0a8a9"

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, apiKey)
    response = requests.get(url)
    responseJSON = response.json()

    return responseJSON["main"]["temp"]


def bot_response(message):
    global cnt
    if cnt == 1:
        answer = "Hi! {}. How old are you?".format(message)
        cnt += 1
        return answer
    elif cnt == 2:
        answer = "You're {} years old. How are you doing?".format(message)
        cnt += 1
        return answer
    elif cnt == 3:
        feelings = ["good", "fine", "great", "awesome", "amazing", "fantastic", "superb", "wonderful", "excellent",
                    "terrific", "fantabulous", "super", "super-duper", "ultra", "wow", "cool", "nice", "great",
                    "pretty good"]
        if message.lower() in feelings:
            answer = "I'm glad to hear that. Wanna play a game?"
        else:
            answer = "I'm sorry to hear that. Wanna play a game?"
        cnt += 1
        return answer
    elif cnt == 4:
        if message.lower() == "yes":
            answer = "Let's play Rock, Paper, Scissors!"
        else:
            answer = "Maybe next time"
        cnt += 1
        return answer
    elif cnt == 5:
        if message.lower() == "rock":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            if computer_choice == "rock":
                answer = "I chose {} it's a tie!".format(computer_choice)
            elif computer_choice == "paper":
                answer = "I chose {} I win!".format(computer_choice)
            else:
                answer = "I chose {} you win!".format(computer_choice)
        elif message.lower() == "paper":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            if computer_choice == "paper":
                answer = "I chose {} it's a tie!".format(computer_choice)
            elif computer_choice == "scissors":
                answer = "I chose {} I win!".format(computer_choice)
            else:
                answer = "I chose {} you win!".format(computer_choice)
        elif message.lower() == "scissors":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            if computer_choice == "scissors":
                answer = "I chose {} it's a tie!".format(computer_choice)
            elif computer_choice == "rock":
                answer = "I chose {} I win!".format(computer_choice)
            else:
                answer = "I chose {} you win!".format(computer_choice)
        else:
            answer = "I don't understand. Let's play again!"
            return answer
        cnt += 1
        return answer + " Would you like to know what's the weather like in your city?"
    elif cnt == 6:
        if message.lower() == "yes":
            answer = "What's your city?"
        else:
            answer = "Okay"
        cnt += 1
        return answer
    elif cnt == 7:
        answer = "The temperature in {} is {} degrees Celsius".format(message, getWeather(message))
        cnt += 1
        return answer


