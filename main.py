tasks = {}


def list():
    for key, value in tasks.items():
        print(f'{key: <10}{value}')


def to_do():
    x = input("What is the task? ")
    y = input("what is the date of this task? ")
    tasks[x] = y

to_do()


def to_do2():
    z = input("Do you have another tasks ? yes or no ")
    if z == "yes":
        to_do()
        to_do2()
    else:
        print("That's all for now")


to_do2()


def list_of_tasks():
    l = input("Do you want to see all tasks? yes or no ")
    if l == "yes":
        list()
    else:
        print("bye")

list_of_tasks()

def complited():
    a = input("which task did you complete? ")
    b = input("From which day? ")
    task2 = tasks[a] = (b) + (" - completed")
    list()
complited()