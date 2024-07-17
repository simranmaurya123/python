# value1=input("please enter your name:\n1.Simran\n2.hella\n3.Scarlet\n")

def gettime():
    import datetime
    return datetime.datetime.now()
def take(k):
     if k==1:
         c=int(input("press 1 for exercise 2 for food: "))
         if c==1:
             value=input("Type here")
             with open("simran exercise.txt","a")as op:
                 op.write(str([str(gettime())])+ " "+ value+"\n")
                 print("entered succesfully")
         elif(c==2):
             value=input("type here:\n")
             with open("simran diet.txt","a") as op:
                 op.write(str([str(gettime())])+ " "+ value+"\n")
                 print("entered succesfully")
     elif k==2:
         c = int(input("press 1 for exercise 2 for food: "))
         if (c==1):
             value=input("type here\n")
             with open ("hella-ex.txt","a") as op:
                 op.write(str([str(gettime())])+ " "+ value+"\n")
                 print("entered succesfully")
         elif c==2:
             value=input("type here\n")
             with open("hella-food.txt","a") as op:
                 op.write(str([str(gettime())])+" "+value+"\n")
                 print("entered succesfully")

         elif k==3:
             c = int(input("press 1 for exercise 2 for food: "))
             if c==1:
                 value = input("type here\n")
                 with open("scarlet-ex.txt","a") as op:
                     op.write(str([str(gettime())]) + " " + value + "\n")
                     print("entered succesfully")
         elif c == 2:
                     value = input("type here\n")
                     with open("scarlet-food.txt", "a") as op:
                         op.write(str([str(gettime())]) + " " + value + "\n")
                         print("entered succesfully")
     else:
            print("please input valid number 1. simran, 2. hella,3.scarlet" )
def retrieve(k):
    if k==1:
        c=input("press 1 for exercise and 2 for food")
        if c==1:
            with open("simran exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("simran diet.txt") as op:
                for i in op:
                    print(i,end="")
        elif k==2:
            c = input("press 1 for exercise and 2 for food")
            if c == 1:
                with open("hella-ex.txt") as op:
                    for i in op:
                        print(i, end="")
            elif c == 2:
                with open("hella-food.txt") as op:
                    for i in op:
                        print(i, end="")
            elif k == 3:
                c = input("press 1 for exercise and 2 for food")
                if c == 1:
                    with open("scarlet-ex-ex.txt") as op:
                        for i in op:
                            print(i, end="")
                elif c == 2:
                    with open("scarlet-food-food.txt") as op:
                        for i in op:
                            print(i, end="")
            else:
                print("please input valid number 1. simran, 2. hella,3.scarlet")
                print("health management")
                a=int(input("press 1 for log and 2 for retrieve"))

    if a==1:
        b=int(input("press 1 for simran 2 for hella 3 for scarlet"))
        take(b)
    else:
        b = int(input("press 1 for simran 2 for hella 3 for scarlet"))
        retrieve(b)


# k1 = int(input("Enter 1 for harry,2 for rohan and 3 for hammad"))
# k2 = int(input("Enter 1 for exercise and 2 for food"))
#
#
# #Date time function for get date and time
# import datetime
# def gettime():
#     return str(datetime.datetime.now())
# #When Take function will get call This one for logging the values of clients
# def Take(a):
#     if a==1:
#         D = int(input("Press 1 for exersise and 2 for food:  "))
#         if D==1:
#             Value= input("Type Here\n")
#             with open("Harryex.txt","a") as op:
#                 op.write(gettime()+' ' +Value)
#                 print("Entered Successfully")
#
#         elif D==2:
#             Value = input("Type Here\n")
#             with open("Harryfoo.txt", "a") as op:
#                 op.write(gettime()+' '+Value)
#                 print("Entered Successfully")
#     elif a==2:
#         D = int(input("Press 1 for exersise and 2 for food:  "))
#         if D == 1:
#             Value = input("Type Here\n")
#             with open("Rohanex.txt", "a") as op:
#                 op.write(gettime()+' '+Value)
#                 print("Entered Successfully")
#
#         elif D == 2:
#             Value = input("Type Here\n")
#             with open("Rohanfoo.txt", "a") as op:
#                 op.write(gettime() + ' ' + Value)
#                 print("Entered Successfully")
#     elif a==3:
#         D = int(input("Press 1 for exersise and 2 for food:  "))
#         if D == 1:
#             Value = input("Type Here\n")
#             with open("Hammadex.txt", "a") as op:
#                 op.write(gettime() + ' ' + Value)
#                 print("Entered Successfully")
#
#         elif D == 2:
#             Value= input("Type Here\n")
#             with open("Hammadfoo.txt", "a") as op:
#                 op.write(gettime() + ' ' + Value)
#                 print("Entered Successfully")
#     else:
#         print("Kindly enter the right choice ex(1-Harry,2-Rohan,3-Hammad): ")
#
# #When Retrieve function will get call, This one for retrieving the values of clients
# def Retrieve(b):
#     if b==1:
#         Value = int(input("Press 1 for exercise and 2 for food: "))
#         if Value == 1:
#             with open("Harryex.txt") as op:
#                 for content in op:
#                     print(content, end="")
#         elif Value == 2:
#             with open("Harryfoo.txt") as op:
#                 for content in op:
#                     print(content, end="")
#     elif b==2:
#         Value = int(input("Press 1 for exercise and 2 for food: "))
#         if Value == 1:
#             with open("Rohanex.txt") as op:
#                 for content in op:
#                     print(content, end="")
#         elif Value == 2:
#             with open("Rohanfoo.txt") as op:
#                 for content in op:
#                     print(content, end="")
#     elif b==3:
#         Value = int(input("Press 1 for exercise and 2 for food: "))
#         if Value == 1:
#             with open("Hammadex.txt") as op:
#                 for content in op:
#                     print(content, end="")
#         elif Value == 2:
#             with open("Hammadfoo.txt") as op:
#                 for content in op:
#                     print(content, end="")
#     else:
#         print("Kindly enter the right choice ex(1-Harry,2-Rohan,3-Hammad): ")
#
#
# # Taking the input from the user
# A = int(input("Press 1 for log the value and 2 for retrieve: "))
# if A==1:
#     B = int(input("Press 1 for Herry, 2 for Rohan, 3 for Hammad: "))
#     Take(B)
# else:
#     C = int(input("Press 1 for Herry, 2 for Rohan, 3 for Hammad: "))
#     Retrieve(C)
#
#

#
