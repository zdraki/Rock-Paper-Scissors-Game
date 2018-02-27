import random
import sys

#lets declare the global count variables
rock_count = 0
paper_count = 0
scissors_count = 0

dictionary = {1:"Paper", 2:"Scissor", 3:"Rock"}

def getUserChoice():

    # declare global variables inside method
    global rock_count
    global paper_count
    global scissors_count
    
#     print "getUserChoice"
#     print rock_count, paper_count, scissors_count

    print("Please enter your choice. 1 for Paper, 2 for Scissors, 3 for Rock or 4 If you would like to quit.")
    
    
    while(True):
        user_choice = raw_input();
        if(user_choice == "4"):
            print("Bye Bye !!!!")
            sys.exit(0)
        elif(user_choice not in ("1","2","3","4")):
            print("Dont be silly!!! Enter a correct choice!")
            continue    
        else:
            #record whatever user chooses in the counts
            if(user_choice=="1"):
                paper_count = paper_count+1
            elif(user_choice=="2"):
                scissors_count = scissors_count+1
            elif(user_choice=="3"):
                rock_count = rock_count+1    
                
            return int(user_choice)
        

def getProbability(count):
    # declare global variables inside method
    global rock_count
    global paper_count
    global scissors_count
    
    if rock_count == 0 and paper_count == 0 and scissors_count == 0:
        return random.random()
    else:
        return (float(count)/float(rock_count+paper_count+scissors_count))

getProbability(2)

def getComputersChoice():
    
    # declare global variables inside method
    global rock_count
    global paper_count
    global scissors_count
    
    p_rock = getProbability(rock_count)
    p_paper = getProbability(paper_count)
    p_scissors = getProbability(scissors_count)
    rand = random.random()
    
#     print "getComputerChoice"
#     print rock_count, paper_count, scissors_count
#     print p_rock, p_paper, p_scissors, rand
    
    if 0.0<=rand and rand <=p_paper:
        return 2
    elif p_paper<=rand and rand <=p_scissors+p_paper:
        return 3
    else:
        return 1        

def playGame():
    global choice_mapping
    computer_choice = getComputersChoice()
    user_choice = getUserChoice()
    
    if(computer_choice == user_choice):
        print("Its a Tie!!!!!! :)")
    elif ((user_choice-computer_choice) %3 ==1):
        print("You won!!!!!! :)")
    else:
        print("You lost!!!")    
    
    print("Computer's choice was " + dictionary[computer_choice] + ". You chose "+ dictionary[user_choice])
    print "*  " * 5

while(True):
    playGame()