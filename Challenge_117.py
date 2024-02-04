import csv
import random

#initialising an empty score counter
score = 0

#asking user for name
name = input("What is your name: ")

#preparing the first question
q1_num1 = random.randint(10, 50)
q1_num2 = random.randint(10, 50)
question1 = str(q1_num1) + " + " + str(q1_num2) + " = "

#asking the first question
ans1 = int(input(question1))
realans1 = q1_num1+q1_num2

#checking the answers
if ans1 == realans1:
    #incrementing the score, if answer is correct
    score = score+1

#preparing the second question
q2_num2 = random.randint(10, 50)
q2_num1 = random.randint(10, 50)
question2 = str(q2_num1) + " + " + str(q2_num2) + " = "

#asking the second question
ans2 = int(input(question2))
realans2 = q2_num1+q2_num2

#checking the answers
if ans2 == realans2:
    #incrementing the scores
    score = score+1

#printing the score
print(f"Congrats {name}, you scored {score} points.")

#adding new information to the file
file = open("QuizScore.csv", "a")
newrecord = name+" , "+question1+" , "+str(ans1)+" , "+question2+" , "+str(ans2)+" , "+str(score)+"\n"
file.write(str(newrecord))

file.close()