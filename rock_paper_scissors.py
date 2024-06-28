import random as rn
user_choice=int(input("enter 0 for rock 1 for paper and 2 for scissor:"))
computer_choice=rn.randint(0,2)
print("computer choice is:",computer_choice)
if user_choice>2 or user_choice<0:
    print("please enter numbers in the range(0,2)")
elif computer_choice==user_choice:
    print("the game is draw")
elif computer_choice==0 and user_choice==2:
    print("you lose") 
elif computer_choice==2 and user_choice==0:
    print("you win")
elif computer_choice>user_choice:
    print("you lose")
elif computer_choice<user_choice:
    print("you win") 
elif user_choice>2:
    print("please enter number in the range(0,2)")