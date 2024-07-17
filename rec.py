def factorial(n):
    """
    :param n:
    :return:
    """
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return fac

def factorial_recursive(n):
    """
    :param n:
    :return:
    """
    if n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)

def fibonacci(n):

    if n==1:
     return 0
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+(n-2)


number = int(input("enter the number: " ))

# print("factorial using iterative method:",factorial(number))
# print("factorial using recursive method:",factorial_recursive(number))
print(fibonacci(number))


# number = int(input("enter the number: " ))
# print(factorial(number))



