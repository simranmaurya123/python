# a=int(input("enter the number"))
#
# if a<10:
#     print("It is a single digit number")
#
# elif a>=10 and a<=100:
#     print("it is double digit number")
#
# else:
#     print("it is a multiple digit number")


a = int(input("enter your first side:\n"))
b = int(input("enter your second side:\n"))
c = int(input("enter your third side:\n"))

if a+b>c and b+c>a and c+a>b:
    print("triangle is possible")
    if (a==b) and (b==c) and (c==a):
      print("it is a equilateral triangle")
    elif (a==b) or (b==c) or (c==a):
      print("it is isoceles triangle ")
    elif (a!=b) and (b!=c) and (c!=a):
      print(" it is scalene triangle")
else:
    print("triangle is not formed")

# # #


# a = int(input("enter a number"))
# facts = 0
# for i in range(1, a+1):
#     if a % i == 0:
#         facts = facts + 1
#     print(i)
#
# print("exiting the loop, fact is: ", facts)
#
# if facts == 2:
#     print("prime number")
# else:
#     print(" it is a composite number")
# #
# #
#
#
# n = int(input('Enter number: '))
# prime = True
# for i in range(2, n):
#     print(n, '%', i, '=', n % i)
#
#     if n % i == 0:
#         prime = False
#         break
#
# if prime == True:
#     print("Prime number")
# else:
#     print("Composit number")


# a=int(input("enter the number in km"))
# print(" jdhihe " , a*1.6)

# a=5%4
# print(a)



# a=4
# b=5
#
# print(b,a)