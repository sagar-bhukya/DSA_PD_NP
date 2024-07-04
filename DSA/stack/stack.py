#stack stores items in last in first out(LIFO)  or First in lastout(FIFO)
'''
basic opeartions of stack:
1.push: add the ele to stack
2.pop: remove ele from the stack
3.peek or top: top ele from the stack
4.isEmpty: wethear the stack is empty or not



realtime application:
1.undo mechanism in Text editors
2.web broweser navigation

'''


stack=[]
def push():
    if len(stack)==n:
        print("stack is full!....")
    else:
        ele=int(input("enter the ele to add: "))
        stack.append(ele)
        print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("remove element: ",e)
        print(stack)
n=int(input("limit of stack.."))
while True:
    print("select the operations 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("please enter correct operation!")
