import time
import random

boardRow1 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow2 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow3 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow4 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow5 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow6 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow7 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow8 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow9 = ["□","□","□","□","□","□","□","□","□","□"]
boardRow10 = ["□","□","□","□","□","□","□","□","□","□"]

print(boardRow1)
print(boardRow2)
print(boardRow3)
print(boardRow4)
print(boardRow5)
print(boardRow6)
print(boardRow7)
print(boardRow8)
print(boardRow9)
print(boardRow10)
print()
print()
print()

start = input()

if start != "":
    start = input()

carrier = 5
Battle_ship = 4
cruiser = 3
Submarine = 3
destroyer = 2

carrier_spot = random.randint(1,6)

carrier_rotation = random.randint(1,2)

if carrier_rotation == 1:
    if carrier_spot == 1:
        boardRow1[0] = "■"
        boardRow1[1] = "■"
        boardRow1[2] = "■"
        boardRow1[3] = "■"
        boardRow1[4] = "■"
    elif carrier_spot == 2:
        boardRow1[1] = "■"
        boardRow1[2] = "■"
        boardRow1[3] = "■"
        boardRow1[4] = "■"
        boardRow1[5] = "■"
    elif carrier_spot == 3:
        boardRow1[2] = "■"
        boardRow1[3] = "■"
        boardRow1[4] = "■"
        boardRow1[5] = "■"
        boardRow1[6] = "■"
    elif carrier_spot == 4:
        boardRow1[3] = "■"
        boardRow1[4] = "■"
        boardRow1[5] = "■"
        boardRow1[6] = "■"
        boardRow1[7] = "■"        
    elif carrier_spot == 5:
        boardRow1[4] = "■"
        boardRow1[5] = "■"
        boardRow1[6] = "■"
        boardRow1[7] = "■"
        boardRow1[8] = "■"   
    elif carrier_spot == 6:
        boardRow1[5] = "■"
        boardRow1[6] = "■"
        boardRow1[7] = "■"
        boardRow1[8] = "■"
        boardRow1[9] = "■"
elif carrier_rotation == 2:
    if carrier_spot == 1:
        boardRow1[0] = "■"
        boardRow2[0] = "■"
        boardRow3[0] = "■"
        boardRow4[0] = "■"
        boardRow5[0] = "■"
    elif carrier_spot == 2:
        boardRow2[0] = "■"
        boardRow3[0] = "■"
        boardRow4[0] = "■"
        boardRow5[0] = "■"
        boardRow6[0] = "■"   
    elif carrier_spot == 3:
        boardRow3[0] = "■"
        boardRow4[0] = "■"
        boardRow5[0] = "■"
        boardRow6[0] = "■"
        boardRow7[0] = "■"        
    elif carrier_spot == 4:
        boardRow4[0] = "■"
        boardRow5[0] = "■"
        boardRow6[0] = "■"
        boardRow7[0] = "■"
        boardRow8[0] = "■"  
    elif carrier_spot == 5:
        boardRow5[0] = "■"
        boardRow6[0] = "■"
        boardRow7[0] = "■"
        boardRow8[0] = "■"
        boardRow9[0] = "■" 
    elif carrier_spot == 2:
        boardRow6[0] = "■"
        boardRow7[0] = "■"
        boardRow8[0] = "■"
        boardRow9[0] = "■"
        boardRow10[0] = "■"         
            
print(boardRow1)
print(boardRow2)
print(boardRow3)
print(boardRow4)
print(boardRow5)
print(boardRow6)
print(boardRow7)
print(boardRow8)
print(boardRow9)
print(boardRow10)
