print("Welcome To Programming Fundamentals (Python) Quiz!!!")

playing = input("Do You Want To Play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Lets play :) ")
score = 0
answer = input("What Does OOP Stands for? ")
if answer.lower() == "object oriented programming":
    print("Correct!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Who is founder of Python? ")
if answer.lower() == "guido van rossum":
    print("Correct!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Is Python Dynamically typed Language or Statically typed Language?? ")
if answer.lower() == "dynamically typed":
    print("Correct!!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("Syntax Type of a variable or object in python? ")
if answer.lower() == "type(variable)":
    print("Correct!!")
    score +=1
else:
    print("Incorrect!!!")
print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/4)*100) + "%." )