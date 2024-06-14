#3,2,4
#0 1 2
def insertion_sort(A):
    n=len(A) #4
    for i in range(1,n):
        next_val=A[i]#3 4
        position=i#1  2
        while position>0 and A[position-1]>next_val:
        #        1>0           3>2 : True
        #        2>0           ``
            A[position]=A[position-1]
            #    A[1]=3
            position =position-1
                    # 0
        A[position]=next_val #2 3
    return A
a=insertion_sort([3,2,4,1])
print(a)


def insert_tasks(tasks):
    n=len(tasks)

    for i in range (1,n):
        current_task=tasks[i]
        position=i
        while position>0 and tasks[position-1]["priority"]>current_task["priority"]:
            tasks[position]=tasks[position-1]
            position =position-1
        tasks[position]=current_task
    return tasks
tasks = [
  {"id": 1, "name": "Fix bug", "priority": "High"},
  {"id": 2, "name": "Write report", "priority": "Medium"},
  {"id": 3, "name": "Review code", "priority": "Low"},
]
# Simulate new tasks arriving
new_task = {"id": 4, "name": "Update documentation", "priority": "High"}
tasks.append(new_task)
a=insert_tasks(tasks)
print(a)


