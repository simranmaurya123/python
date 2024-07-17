print("how many rows you want\n ")
num=int(input())
print("enter 1 or 0")
value=input("1 for true 0 for false:\n")
if value=="1":
    for i in range(0,num+1):
        print("*"*num(i))
if value =="0":
    for i in range(num,0,-1):
        print("*"*int(i))

def take(k):
if k==1:
  c=int(input("press 1 for exercise 2 for food: "))
if c==1:
             value=input("Type here")
with open("simran exercise.txt","a")as op:

            op.write("value")
print("entered succesfully")



