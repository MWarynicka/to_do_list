tasks = {}
def table_of_tasks():
    tasks={}
    headers = ['Tasks', 'Data']
    print(f'{headers[0]: <10}{headers[1]}')
    for key, value in tasks:
      print(f'{key: <10}{value[0]: <15}{value[1]}')
table_of_tasks()
