import time
xd="💀☠️🐴🔱⚜️⚫⚪♟️🗜️🏢🛕🗼✝️⬛⬜◼️◻️"
b=[["bR","bN","bB","bQ","bK","bB","bN","bR"],
   ["bp","bp","bp","bp","bp","bp","bp","bp"],
   [",,","..",",,","..",",,","..",",,",".."],
   ["..",",,","..",",,","..",",,","..",",,"], 
   [",,","..",",,","..",",,","..",",,",".."], 
   ["..",",,","..",",,","..",",,","..",",,"],
   ["wp","wp","wp","wp","wp","wp","wp","wp"],
   ["wR","wN","wB","wQ","wK","wB","wN","wR"]
   ]
black_pieces={"R1":["bR",[0,0],[]],"p1":["bp",[0,1],[]],"p2":["bp",[1,1],[]],"p3":["bp",[2,1],[]],"p4":["bp",[3,1],[]],"p5":["bp",[4,1],[]],"p6":["bp",[5,1],[]],"p7":["bp",[6,1],[]],"p8":["bp",[7,1],[]]}
white_pieces={"p1":["wp",[0,6],[]],"p2":["wp",[1,6],[]],"p3":["wp",[2,6],[]],"p4":["wp",[3,6],[]],"p5":["wp",[4,6],[]],"p6":["wp",[5,6],[]],"p7":["wp",[6,6],[]],"p8":["wp",[7,6],[]]}
dictionary={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
def checkPossibleMoves(p):
    if white_pieces[p][0]=="wp":
        if white_pieces[p][1][1]==6:
            white_pieces[p][2].append(f"{dictionary[white_pieces[p][1][0]]}{8-white_pieces[p][1][1]+2}")
        white_pieces[p][2].append(f"{dictionary[white_pieces[p][1][0]]}{8-white_pieces[p][1][1]+1}")
    if black_pieces[p][0]=="bp":
        if black_pieces[p][1][1]==1:
            black_pieces[p][2].append(f"{dictionary[black_pieces[p][1][0]]}{8-black_pieces[p][1][1]-2}")
        black_pieces[p][2].append(f"{dictionary[black_pieces[p][1][0]]}{8-black_pieces[p][1][1]-1}")
    if black_pieces[p][0]=="bR":
        for i in range(black_pieces[p][1][0],8): # up 
            if b[i][black_pieces[p][1][1]]!=".." and False or b[i][black_pieces[p][1][1]]!=",," and False:
                break
            black_pieces[p][2].append(f"{dictionary[black_pieces[p][i][black_pieces[p][1][1]]]}{8-black_pieces[p][1][1]-1}")
        for i in range(black_pieces[p][1][0],-1,-1): # down 
            if b[i][black_pieces[p][1][1]]!=".." or b[i][black_pieces[p][1][1]]!=",,":
                break
            black_pieces[p][2].append(f"{dictionary[black_pieces[p][i][black_pieces[p][1][1]]]}{8-black_pieces[p][1][1]-1}")

    if black_pieces[p][0]=="bN":
        for i in range(black_pieces[p][1][0],8):
            if b[i][black_pieces[p][1][1]]!=".." or b[i][black_pieces[p][1][1]]!=",,":
                break
            black_pieces[p][2].append(f"{dictionary[black_pieces[p][1][0]]}{8-black_pieces[p][1][1]-1}")


for i in range(1,9):
    checkPossibleMoves(f"p{i}")
    
checkPossibleMoves("R1")

print(white_pieces)
print(black_pieces)

def printM():
    print("----------------------------")
    for i in range(8):
        for j in range(8):
            print(f"{b[i][j]}  ",end="")
        print("")
    print("-------------------------")

def swap(x_i,y_i,x_f,y_f):
    c=b[x_i][y_i]
    if (x_i+y_i)%2==0:
        b[x_i][y_i]=".."  
    else: 
        b[x_i][y_i]=",," 
    b[x_f][y_f]=c

"""
printM()
time.sleep(1)
swap(6,0,4,0)#a2- a4
printM()
time.sleep(1)
swap(0,1,2,2)
printM()
"""

x=0
y=0
printM()
move=input("Move: ")
if(move[0]!="B" and move[0]!="R" and move[0]!="Q" and move[0]!="N" and move[0]!="K"):
    for i in white_pieces:
        print(i)
printM()
