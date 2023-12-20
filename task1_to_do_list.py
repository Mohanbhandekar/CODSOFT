task=[]
status=[]
t=0
def disp():
    print("sr no.         status                  Task             \n")
    for i in range(len(task)):
        print("  ",(str(i+1)).ljust(12," "),end="")
        print(status[i].ljust(22," "),end="")
        print(task[i],"\n")
def create():
    t=int(input("Enter number of Task : "))
    for i in range(t):
        status.append("unknown")
        temp=input("Enter task : ")
        task.append(temp)
    disp()

create()

while(True):
    print("press key    update->1   create new list->2    End program->3")
    k=int(input())
    if(k==1):
        print("add task ->1")
        print("update status ->2")
        k1=int(input())
        if(k1==1):
            create()
        elif(k1==2):
            no=int(input("Enter task no : "))
            stemp=int(input("completed->1  Not completed->2 "))
            if(stemp==1):
                status[no-1]="completed"
            else:
                status[no-1]="Not completed"
            disp()
    elif(k==2):
        task.clear()
        status.clear()
        create()
    elif(k==3):
        break


    
    
    
