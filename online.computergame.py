
print("welcome to my online computer quiz game!")
playing = input("do you want to play? ")
if playing.lower()!= "yes":
    quit()
print("okay let's play :) ")
score = 0

# question 1
question = input("what is ML? ")
if question.lower() == "machine learning":
    score += 1
    print("correct!")
else:
    print("incorrect")

# question 2
question2 = input("what is CPU? ")
if question2.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("sorry better luck next time :(" )

# question 3
question3 = input("what is AI? ")
if question3.lower()== "artificial intelligence" :
    print("correct")
    score += 1
else:
    print("incorrect")

# question4
question4 = input("what does a machine do? ")
if question4 == "it reduces human time and gives efficient results":
    print("correct! ")
    score += 1
else:
    print("incorrect")
# question5
question5 = input("what is the CU? " )
if question5.lower() == "control unit":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got "+ str(score) + " correct answers ")
print("you got "+ str((score/5)*100) + "%.")






