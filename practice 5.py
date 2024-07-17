customers = ["Simran", "Hella", "Scarlet"]


def datetime():
    import datetime
    return datetime.datetime.now()


def log(file_name, sentence):
    with open(file_name, "a") as op:
        op.write("["+str(datetime())+"] "+sentence + "\n")


def retrieve(file_name):
    with open(file_name,"r") as op:
       print(op.read())


def log_diet(sname,diet_name):
    print("log diet for " + customers[sname-1])
    filename="log_diet_" + customers[sname-1]+".txt"
    log(filename,   diet_name)


def log_exercise(sname,exercise_name):
    print("log exercise for " + customers[sname-1])
    filename = "log_exercise_" + customers[sname - 1] + ".txt"
    log(filename,  exercise_name)


def retrieve_diet(sname):
    print("retrieve diet for " + customers[sname-1])
    filename = "log_diet_"+ customers[sname-1]+".txt"
    retrieve(filename)




def retrieve_exercise(sname):
    print("retrieve exercise for " + customers[sname-1])
    filename = "log_exercise_" + customers[sname-1] + ".txt"
    retrieve(filename)



action_type = int(input("What do you want to do, log or retrieve?\npress 1 for log and 2 for retrieve "))

diet_exercise = int(input("Enter 1 for  diet and 2 for exercise"))

selected_name = int(input("press 1 for simran 2 for hella 3 for scarlet"))



if action_type == 1:



    if diet_exercise == 1:  # 1 for diet
        dietname=input("enter diet name")
        log_diet(selected_name, dietname)
    else:
        exercisename=input("enter exercise name")
        log_exercise(selected_name,exercisename)




else:


    if diet_exercise == 1:

        retrieve_diet(selected_name)
    else:
        retrieve_exercise(selected_name)
