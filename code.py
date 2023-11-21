print("Welcome to the Quiz game")

play = input("Do you want to play the game?")
score = 0

if play.lower() != "yes":
    quit()

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does FIFO stand for? ").lower()
if answer == "first in first out":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str((score/5) * 100) + "%" + " marks!") 
