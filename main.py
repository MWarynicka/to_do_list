tasks = {}
def table_of_tasks(tasks2):
    tasks2={}
    tasks= tasks2
    for key, value in tasks2.items():
        print(f'{key: <10}{value}')
table_of_tasks()

def to_do():
    x = input("What is the task? ")
    y = input("what is the date of this task? ")
    tasks[x] = y


to_do()
def to_do2():
    z = input("Do you have another tasks ? yes or no ")
    if z == "yes" :
        to_do()
        to_do2()
    else:
        print("That's all for now")

to_do2()

def list_of_tasks():
    l= input("Do you want to see all tasks? Yes or No ")
    if l == "Yes":
        table_of_tasks()

    else:
        print("Bye")

list_of_tasks()








