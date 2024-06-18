import random
user_wins=0
computer_wins=0
options=["Rock","Paper","Scissor"]
while True:
    user_input = input("Type Rock/Paper/Scissor (Or) Q to Quit:");
    if user_input=="Q" or user_input=="q":
        print("Game Over!")
        break
    if user_input  not in ["Rock","Paper","Scissor"]:
        continue
    random_number=random.randint(0,2)
    computer_input=options[random_number]
    print("Computer Picked",computer_input)
    
    if user_input=="Rock" and computer_input=="Scissor":
         print("You Won!")
         user_wins+=1
    elif user_input=="Paper" and computer_input=="Rock":
         print("You Won!")
         user_wins+=1
    elif user_input=="Scissor" and computer_input=="Paper":
         print("You Won!")
         user_wins+=1   
    else:
        print("You Lost!")
        computer_wins+=1
        
print("Your Score:",user_wins)
print("Computer Score:",computer_wins)
if user_wins>computer_wins:
    print("You Won!")
elif user_wins<computer_wins:
    print("You Lost!")    
elif user_wins==computer_wins:
    print("Tie")
print("GoodBye!")