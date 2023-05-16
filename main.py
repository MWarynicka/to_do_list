tasks = {}
def to_do():
    x = input("What is the task? ")
    y = input("What is the deadline? ")
    tasks[x] = y
    print(tasks)

to_do()
def to_do2():
    z = input("Do you have another tasks ? yes or no ")
    if z == "yes" :
        to_do()
        to_do2()
    else:
        print("That's all for now")

to_do2()




