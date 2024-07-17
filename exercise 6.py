# #Game
import random
lst = ["snake", "water", "gun"]


computer_point = 0
human_point = 0
a=10
i=0
while i<a:
   player_choice = int(input("press 1 for snake 2 for water 3 for gun: \n"))
   choice = random.choice(lst)

   if player_choice == choice:
    print("draw both got 0 point")

   elif player_choice==1 and choice=="water":
     human_point=human_point+1
     print("you won")
     print(f"computer point is {computer_point} and your point is {human_point}")


   elif player_choice==1 and choice=="gun":
     computer_point=computer_point+1
     print("you lose")
     print(f"computer point is {computer_point} and your point is {human_point}")

   elif player_choice==2 and choice=="snake":
     computer_point = computer_point + 1
     print("you lose")
     print(f"computer point is {computer_point} and your point is {human_point}")



   elif player_choice==2 and choice=="gun":
      human_point = human_point + 1
      print("you won")
      print(f"computer point is {computer_point} and your point is {human_point}")


   elif player_choice==3 and choice=="snake":
     human_point = human_point + 1
     print("you won")
     print(f"computer point is {computer_point} and your point is {human_point}")


   elif player_choice ==3 and choice=="water":
      computer_point = computer_point + 1
      print("you lose")
      print(f"computer point is {computer_point} and your point is {human_point}")


   else:
    print("invalid input")

   i=i+1
   print(f"{a-i} is left out of {a}")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")







