def vaccum():
    state = { 'A' : 0 , 'B' : 0}
    cost = 0
    vacum = input("Enter location of vaccum :")
    state['A'] = int(input("Enter 1 if A room is dirty else enter 0: "))
    state['B'] = int(input("Enter 1 if B room is dirty else enter 0: "))
    if vacum =='A' :
        print("Vaccum is in A room")
        if(state['A']==1):
            cost= cost+2
            state['A']=0
            print("Room A is cleaned :")
            print("Vacum cleaner moved to room B")
            if(state['B']==1):
                cost = cost +1
                print("Room B is cleaned :")
        else:
            cost = cost + 1
            print("Vacum cleaner moved to room B as room A is already clean ")
            if(state['B']==1):
                cost = cost + 1
                print("Room B is cleaned :")
    if vacum =='B' :
        print("Vaccum is in B room")
        if(state['B']==1):
            cost= cost+2
            state['B']=0
            print("Room B is cleaned :")
            print("Vacum cleaner moved to room A")
            if(state['A']==1):
                cost = cost +1
                print("Room A is cleaned :")
        else:
            cost = cost + 1
            print("Vacum cleaner moved to room A as room B is already clean ")
            if(state['A']==1):
                cost = cost + 1
                print("Room A is cleaned :")
    print("cost to perform the cleaning process is",cost)
vaccum()