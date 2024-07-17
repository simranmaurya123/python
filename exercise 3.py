# s=18
# i=0
# a=6
# print("please guess the number from 1to 20\n yo can try only 5 times")
# while i <5:
#     i=i+1
#     a=a-1
#     print("you are left with",a, " tries\n Enter number:")
#     guess=int(input())
#     if guess>s:
#      print("you have guessed a greater number")
#     elif guess ==s:
#      print("congrats! you won")
#      break
#     else :
#      print("you have guessed a lesser number" )
# if i==5:
#       print("Game over")


n=18
i=0
a=6

print("guess the number from 1 to 20 \n u can try only 5 times")

while i<5:
    i= i + 1
    a=a-1
    print("you are left with ",a, "tries \n Enter number:")
    guess =int(input())
    if guess<n:
        print("Enter a larger no.")
    elif guess==n:
        print("congrats you won")
        break
    else:
        print("Enter a smaller no.")
if i==5:
    print("Game over")

























