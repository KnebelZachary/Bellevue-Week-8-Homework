#sample file to have in repo for assignement

from time import sleep

print("This is a sample Python project")

question1 = "Type a message and I will repeat it back to you! (Type 'quit' to end the program):"

while True:
    message = input (question1)
    if  message == "quit":
        print("Thanks for playing!")
        break
    else:
        print(message)
        sleep(2)