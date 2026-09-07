map1=[["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ]
ships=[2]
map2=[["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ["·","·","·","·","·","·","·","·" ],
      ]

def printM(M):
    print("-----------")
    for i in range(8):
        for j in range(8):
            print(M[i][j],end="")
        print()
    print("-----------")

def set1(S,m):
    for i in S:
        succ=False
        while not succ:
            print(f"Length: {i}")
            c=int(input("Select column (0-7): "))
            s=int(input("Select start (0-7): "))
            o=input("Select orientation (w/H): ")
            o.lower()
            interr=False
            if i+s-1<=7 and c+i-1<=7: # if fits on the board
                if o=="h":
                    for j in range(i): # not 
                        if m[s+j][c]=="S":
                            print("Error: Interruption by other ship")
                            interr=True
                    if not interr:
                        for j in range(i):
                            m[s+j][c]="S"
                        succ=True
                elif o=="w":
                    for j in range(i):
                        if m[s][c+j]=="S":
                            print("Error: Interruption by other ship")
                            interr=True
                    if not interr:
                        for j in range(i):
                            m[s][c+j]="S"
                        succ=True
            else:
                succ=False
                print("Error: Out of range")

def attack(r,c,map):
    if map[r][c]=="S":
        map[r][c]="X"
        print("Shot")
    else:
        map[r][c]="O"
        print("Fail")

def checkdeath(m):
    for i in range(8):
        for j in range(8):
            if m[i][j]=="S":
                return False
    return True

def set2(S):
    pass

def start():
    print("Player 1: ")
    set1(ships,map1)
    print("Player 2: ")
    set1(ships,map2)

    print("Player 1: ")
    printM(map1)
    print("Player 2: ")
    printM(map2)    

    turn=1
    theEnd=False
    while not theEnd:
        print(f"Turn: {turn}")
        if turn==1:
            r=int(input("Row: "))
            c=int(input("Column: "))
            attack(r,c,map2)
            turn=2
        else:            
            r=int(input("Row: "))
            c=int(input("Column: "))
            attack(r,c,map1)
            turn=1
        if checkdeath(map1) or checkdeath(map2):
            theEnd=True
    if checkdeath(map1):
        print("Winner Player 2")    
    else:
        print("Winner Player 1")
    printM(map1)
    printM(map2)



start()
