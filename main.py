import random
import time
import os

game = ['rock','paper','scissors']

while True:
    os.system('cls')
    print("Start getting you hands in Motion!!!")
    time.sleep(1)
    temp = game[random.randrange(0,2)]

    for i in game:
        print(i,"!")
        time.sleep(0.5)

    print(f">>>{temp}")

    userInput= input("\nDo you want to play another game?(y/n) ")

    if userInput.lower() == "y":
        continue
    if userInput.lower() == "n":
        exit()
    else:
        continue