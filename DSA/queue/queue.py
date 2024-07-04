# the queues store the data in First in first out(FIFO) or Last in Last out(LILO)



#enqueue: append the ele to queue
#dequeue: pop from the queue. we are not removing the ele from the last. so list.pop(0) from first what we have added first



que=[]
def enqueue():
    if len(que)==n:
        print("que is full......")
    else:
        el=int(input("enter the elem: "))
        que.append(el)
def dequeue():
    if not que:
        print("queue is empty ...")
    else:
        e=que.pop(0)
        print("the ele is removed from the ",e)
def display():
    print(que)


n=int(input("how much que do you want to enter"))
while True:
    print("Select operations 1.enqueue 2.dequeue 3.show 4. quit")
    choice=int(input())

    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("please enter the correct operation")

