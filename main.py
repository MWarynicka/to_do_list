tasks = {}


def list():
    for key, value in tasks.items():
        print(f'{key: <10}{value}')


def to_do():
    x = input("What is the task? ").lower()
    y = input("what is the date of this task? ")
    tasks[x] = y

to_do()


def to_do2():
    z = input("Do you have another tasks ? yes or no ").lower()
    if z == "yes":
        to_do()
        to_do2()
    elif z == "no":
        print("That's all for now")
    else:
        print("\nThat is incorrect, please try again.\n")


to_do2()


def list_of_tasks():
    l = input("Do you want to see all tasks? yes or no ").lower()
    if l == "yes":
        list()
    elif l == "no":
        print("bye")
    else:
        print("\nThat is incorrect, please try again.\n")

list_of_tasks()

def complited():
    a = input("which task did you complete? ").lower()
    b = input("From which day? ")
    task2 = tasks[a] = (b) + (" - completed")
    c = input("Have another completed task? yes or no ")
    if c == "yes":
        complited()
    else:
        list()
        print("See you soon!")

complited()