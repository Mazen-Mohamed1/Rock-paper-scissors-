import random

list = ["rock", "paper", "scissors"]

# welcoming
print("welcome to the Rock, paper, Scissors game :) ")
answer = input("Press [Enter] to Continue or type (Help) for the rules: ").capitalize()



# the users choices
if answer == "Help":
    print("""
            *************** RULES  ****************
            1) you choose and the computer chooses
            2) Rock smashes Scissors -> Rock wins
            3) Scissors cut Paper -> Scissors win
            4) paper Covers Rock -> paper wins
    """)
paper = """
     _______            
---'    ____)____      
           ______)     
          _______)   
         _______)     
---.__________)          
        """

scissors = """
     ______                
---'   ____)____      
          ______)          
       __________)      
      (____)               
---.__(___)                
        """

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

         """

# the game
user = input("Enter your choice (rock, paper, scissors): ").lower()

computer = random.choice(list)

if user not in list:
    print("Invalid choice. Please run the program again and choose rock, paper, scissors.")

print(f"you choose: {user}")
print(eval(user))
print(f"computer choose: {computer}")
print(eval(computer))

# possibilities
if (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissors") or (user == "scissors" and computer == "rock"):
    print("you Lose")
elif user == computer:
    print("it's tie")

else:
    print("you Win")

