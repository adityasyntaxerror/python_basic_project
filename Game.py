
import random
rock=(''' _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
paper=('''_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')
scissor=('''  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
game_images=[rock,paper,scissor]
a=int(input("welcome to our game,choose 0 for rock,1 for paper and 2 for scissor?\n"))
print("You choose")
print(game_images[a])
computer_choice=random.randint(0,2)
print("computer chose")
print(game_images[computer_choice])
if a >= 3 or a < 0:
        print("Invalid number . plz choose again")
elif a==2 and computer_choice==1:
    print("you win")
elif a==1 and computer_choice==0:
    print("User wins.")
elif a==2 and computer_choice==0:
    print("Computer wins")
elif a==0 and computer_choice==2:
    print("user wins.")
elif a==computer_choice:
    print("its draw.")
elif computer_choice>a:
    print("computer wins.")
elif a >= 3 or a < 0:
        print("Invalid number . plz choose again")






















