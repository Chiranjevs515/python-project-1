print("Welcome to computer quiz!")
playing=input("Do you want to play? ")
if(playing.lower()!="yes"):
    print("Thanku!")
    quit()
print("Ok let's play!")
score=0
que=input("What does CPU stands for ? ")
if(que.lower()=="central processing unit"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
que=input("What does RAM stands for ? ")
if(que.lower()=="random access memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("What does ROM stands for ? ")
if(que.lower()=="read only memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("What does GPU stands for ? ")
if(que.lower()=="graphics processing unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("What does CU stands for ? ")
if(que.lower()=="control unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("What does ALU stands for ? ")
if(que.lower()=="arithmetic logical unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("What does IOT stands for ? ")
if(que.lower()=="internet of things"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("What does CD stands for ? ")
if(que.lower()=="compact disk"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
que=input("When does python was developed? ")
if(que.lower()=="1989"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got",score,"out of 9")
print("You got",round((score*100/9),2),"%")
