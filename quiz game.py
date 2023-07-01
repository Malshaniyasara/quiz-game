print('Welcome to my computer quiz!')

playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect answer.")

answer = input("What is the brain of a computer system called? ")
if answer.lower() == "cpu":
    print('Correct!')
    score += 1
else:
    print("Incorrect answer.")

answer = input("Who is considered the father of the computer? ")
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect answer.")

answer = input("What does ALU stand for? ")
if answer.lower() == "arithmetic-logic unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect answer.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random-access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect answer.")

print("You got " + str(score) + " question(s) correct.")
print("You got " + str((score/4)*100) + " question(s) correct.")

