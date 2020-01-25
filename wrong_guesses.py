import datetime
import random
import json

player = input("Hi, what is your name? ")
secret = random.randint(1,30)
attempts = 0

with open("score_list.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict["date"] + score_dict["player_name"])

wrong_guesses = []
while True:
    guess = int(input("Guess the secret number between 1 and 30: "))
    attempts = attempts + 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player, "wrong_guesses": wrong_guesses})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You have guessed it - congratulations! Its number: " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct. Try something smaller.")
    elif guess < secret:
        print("Your guess is nost correct. Try something bigger.")

    wrong_guesses.append(guess)