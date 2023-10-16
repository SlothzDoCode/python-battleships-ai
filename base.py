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

carrier_spotH = random.randint(1,6)

carrier_spotV = random.randint(1,10)

carrier_rotation = random.randint(1,2)

if carrier_rotation == 1:
    if carrier_spotV == 1:
        if carrier_spotH == 1:
            boardRow1[0] = "■"
            boardRow1[1] = "■"
            boardRow1[2] = "■"
            boardRow1[3] = "■"
            boardRow1[4] = "■"
        elif carrier_spotH == 2:
            boardRow1[1] = "■"
            boardRow1[2] = "■"
            boardRow1[3] = "■"
            boardRow1[4] = "■"
            boardRow1[5] = "■"
        elif carrier_spotH == 3:
            boardRow1[2] = "■"
            boardRow1[3] = "■"
            boardRow1[4] = "■"
            boardRow1[5] = "■"
            boardRow1[6] = "■"
        elif carrier_spotH == 4:
            boardRow1[3] = "■"
            boardRow1[4] = "■"
            boardRow1[5] = "■"
            boardRow1[6] = "■"
            boardRow1[7] = "■"        
        elif carrier_spotH == 5:
            boardRow1[4] = "■"
            boardRow1[5] = "■"
            boardRow1[6] = "■"
            boardRow1[7] = "■"
            boardRow1[8] = "■"   
        elif carrier_spotH == 6:
            boardRow1[5] = "■"
            boardRow1[6] = "■"
            boardRow1[7] = "■"
            boardRow1[8] = "■"
            boardRow1[9] = "■"       
    elif carrier_spotV == 2:
        if carrier_spotH == 1:
            boardRow2[0] = "■"
            boardRow2[1] = "■"
            boardRow2[2] = "■"
            boardRow2[3] = "■"
            boardRow2[4] = "■"
        elif carrier_spotH == 2:
            boardRow2[1] = "■"
            boardRow2[2] = "■"
            boardRow2[3] = "■"
            boardRow2[4] = "■"
            boardRow2[5] = "■"
        elif carrier_spotH == 3:
            boardRow2[2] = "■"
            boardRow2[3] = "■"
            boardRow2[4] = "■"
            boardRow2[5] = "■"
            boardRow2[6] = "■"
        elif carrier_spotH == 4:
            boardRow2[3] = "■"
            boardRow2[4] = "■"
            boardRow2[5] = "■"
            boardRow2[6] = "■"
            boardRow2[7] = "■"        
        elif carrier_spotH == 5:
            boardRow2[4] = "■"
            boardRow2[5] = "■"
            boardRow2[6] = "■"
            boardRow2[7] = "■"
            boardRow2[8] = "■"   
        elif carrier_spotH == 6:
            boardRow2[5] = "■"
            boardRow2[6] = "■"
            boardRow2[7] = "■"
            boardRow2[8] = "■"
            boardRow2[9] = "■"
    elif carrier_spotV == 3:
        if carrier_spotH == 1:
            boardRow3[0] = "■"
            boardRow3[1] = "■"
            boardRow3[2] = "■"
            boardRow3[3] = "■"
            boardRow3[4] = "■"
        elif carrier_spotH == 2:
            boardRow3[1] = "■"
            boardRow3[2] = "■"
            boardRow3[3] = "■"
            boardRow3[4] = "■"
            boardRow3[5] = "■"
        elif carrier_spotH == 3:
            boardRow3[2] = "■"
            boardRow3[3] = "■"
            boardRow3[4] = "■"
            boardRow3[5] = "■"
            boardRow3[6] = "■"
        elif carrier_spotH == 4:
            boardRow3[3] = "■"
            boardRow3[4] = "■"
            boardRow3[5] = "■"
            boardRow3[6] = "■"
            boardRow3[7] = "■"        
        elif carrier_spotH == 5:
            boardRow3[4] = "■"
            boardRow3[5] = "■"
            boardRow3[6] = "■"
            boardRow3[7] = "■"
            boardRow3[8] = "■"   
        elif carrier_spotH == 6:
            boardRow3[5] = "■"
            boardRow3[6] = "■"
            boardRow3[7] = "■"
            boardRow3[8] = "■"
            boardRow3[9] = "■"        
    elif carrier_spotV == 4:
        if carrier_spotH == 1:
            boardRow4[0] = "■"
            boardRow4[1] = "■"
            boardRow4[2] = "■"
            boardRow4[3] = "■"
            boardRow4[4] = "■"
        elif carrier_spotH == 2:
            boardRow4[1] = "■"
            boardRow4[2] = "■"
            boardRow4[3] = "■"
            boardRow4[4] = "■"
            boardRow4[5] = "■"
        elif carrier_spotH == 3:
            boardRow4[2] = "■"
            boardRow4[3] = "■"
            boardRow4[4] = "■"
            boardRow4[5] = "■"
            boardRow4[6] = "■"
        elif carrier_spotH == 4:
            boardRow4[3] = "■"
            boardRow4[4] = "■"
            boardRow4[5] = "■"
            boardRow4[6] = "■"
            boardRow4[7] = "■"        
        elif carrier_spotH == 5:
            boardRow4[4] = "■"
            boardRow4[5] = "■"
            boardRow4[6] = "■"
            boardRow4[7] = "■"
            boardRow4[8] = "■"   
        elif carrier_spotH == 6:
            boardRow4[5] = "■"
            boardRow4[6] = "■"
            boardRow4[7] = "■"
            boardRow4[8] = "■"
            boardRow4[9] = "■"
    elif carrier_spotV == 5:
        if carrier_spotH == 1:
            boardRow5[0] = "■"
            boardRow5[1] = "■"
            boardRow5[2] = "■"
            boardRow5[3] = "■"
            boardRow5[4] = "■"
        elif carrier_spotH == 2:
            boardRow5[1] = "■"
            boardRow5[2] = "■"
            boardRow5[3] = "■"
            boardRow5[4] = "■"
            boardRow5[5] = "■"
        elif carrier_spotH == 3:
            boardRow5[2] = "■"
            boardRow5[3] = "■"
            boardRow5[4] = "■"
            boardRow5[5] = "■"
            boardRow5[6] = "■"
        elif carrier_spotH == 4:
            boardRow5[3] = "■"
            boardRow5[4] = "■"
            boardRow5[5] = "■"
            boardRow5[6] = "■"
            boardRow5[7] = "■"        
        elif carrier_spotH == 5:
            boardRow5[4] = "■"
            boardRow5[5] = "■"
            boardRow5[6] = "■"
            boardRow5[7] = "■"
            boardRow5[8] = "■"   
        elif carrier_spotH == 6:
            boardRow5[5] = "■"
            boardRow5[6] = "■"
            boardRow5[7] = "■"
            boardRow5[8] = "■"
            boardRow5[9] = "■"
    elif carrier_spotV == 6:
        if carrier_spotH == 1:
            boardRow6[0] = "■"
            boardRow6[1] = "■"
            boardRow6[2] = "■"
            boardRow6[3] = "■"
            boardRow6[4] = "■"
        elif carrier_spotH == 2:
            boardRow6[1] = "■"
            boardRow6[2] = "■"
            boardRow6[3] = "■"
            boardRow6[4] = "■"
            boardRow6[5] = "■"
        elif carrier_spotH == 3:
            boardRow6[2] = "■"
            boardRow6[3] = "■"
            boardRow6[4] = "■"
            boardRow6[5] = "■"
            boardRow6[6] = "■"
        elif carrier_spotH == 4:
            boardRow6[3] = "■"
            boardRow6[4] = "■"
            boardRow6[5] = "■"
            boardRow6[6] = "■"
            boardRow6[7] = "■"        
        elif carrier_spotH == 5:
            boardRow6[4] = "■"
            boardRow6[5] = "■"
            boardRow6[6] = "■"
            boardRow6[7] = "■"
            boardRow6[8] = "■"   
        elif carrier_spotH == 6:
            boardRow6[5] = "■"
            boardRow6[6] = "■"
            boardRow6[7] = "■"
            boardRow6[8] = "■"
            boardRow6[9] = "■"
    elif carrier_spotV == 7:
        if carrier_spotH == 1:
            boardRow7[0] = "■"
            boardRow7[1] = "■"
            boardRow7[2] = "■"
            boardRow7[3] = "■"
            boardRow7[4] = "■"
        elif carrier_spotH == 2:
            boardRow7[1] = "■"
            boardRow7[2] = "■"
            boardRow7[3] = "■"
            boardRow7[4] = "■"
            boardRow7[5] = "■"
        elif carrier_spotH == 3:
            boardRow7[2] = "■"
            boardRow7[3] = "■"
            boardRow7[4] = "■"
            boardRow7[5] = "■"
            boardRow7[6] = "■"
        elif carrier_spotH == 4:
            boardRow7[3] = "■"
            boardRow7[4] = "■"
            boardRow7[5] = "■"
            boardRow7[6] = "■"
            boardRow7[7] = "■"        
        elif carrier_spotH == 5:
            boardRow7[4] = "■"
            boardRow7[5] = "■"
            boardRow7[6] = "■"
            boardRow7[7] = "■"
            boardRow7[8] = "■"   
        elif carrier_spotH == 6:
            boardRow7[5] = "■"
            boardRow7[6] = "■"
            boardRow7[7] = "■"
            boardRow7[8] = "■"
            boardRow7[9] = "■"
    elif carrier_spotV == 8:
        if carrier_spotH == 1:
            boardRow8[0] = "■"
            boardRow8[1] = "■"
            boardRow8[2] = "■"
            boardRow8[3] = "■"
            boardRow8[4] = "■"
        elif carrier_spotH == 2:
            boardRow8[1] = "■"
            boardRow8[2] = "■"
            boardRow8[3] = "■"
            boardRow8[4] = "■"
            boardRow8[5] = "■"
        elif carrier_spotH == 3:
            boardRow8[2] = "■"
            boardRow8[3] = "■"
            boardRow8[4] = "■"
            boardRow8[5] = "■"
            boardRow8[6] = "■"
        elif carrier_spotH == 4:
            boardRow8[3] = "■"
            boardRow8[4] = "■"
            boardRow8[5] = "■"
            boardRow8[6] = "■"
            boardRow8[7] = "■"        
        elif carrier_spotH == 5:
            boardRow8[4] = "■"
            boardRow8[5] = "■"
            boardRow8[6] = "■"
            boardRow8[7] = "■"
            boardRow8[8] = "■"   
        elif carrier_spotH == 6:
            boardRow8[5] = "■"
            boardRow8[6] = "■"
            boardRow8[7] = "■"
            boardRow8[8] = "■"
            boardRow8[9] = "■"    
    elif carrier_spotV == 9:
        if carrier_spotH == 1:
            boardRow9[0] = "■"
            boardRow9[1] = "■"
            boardRow9[2] = "■"
            boardRow9[3] = "■"
            boardRow9[4] = "■"
        elif carrier_spotH == 2:
            boardRow9[1] = "■"
            boardRow9[2] = "■"
            boardRow9[3] = "■"
            boardRow9[4] = "■"
            boardRow9[5] = "■"
        elif carrier_spotH == 3:
            boardRow9[2] = "■"
            boardRow9[3] = "■"
            boardRow9[4] = "■"
            boardRow9[5] = "■"
            boardRow9[6] = "■"
        elif carrier_spotH == 4:
            boardRow9[3] = "■"
            boardRow9[4] = "■"
            boardRow9[5] = "■"
            boardRow9[6] = "■"
            boardRow9[7] = "■"        
        elif carrier_spotH == 5:
            boardRow9[4] = "■"
            boardRow9[5] = "■"
            boardRow9[6] = "■"
            boardRow9[7] = "■"
            boardRow9[8] = "■"   
        elif carrier_spotH == 6:
            boardRow9[5] = "■"
            boardRow9[6] = "■"
            boardRow9[7] = "■"
            boardRow9[8] = "■"
            boardRow9[9] = "■"    
    elif carrier_spotV == 10:
        if carrier_spotH == 1:
            boardRow10[0] = "■"
            boardRow10[1] = "■"
            boardRow10[2] = "■"
            boardRow10[3] = "■"
            boardRow10[4] = "■"
        elif carrier_spotH == 2:
            boardRow10[1] = "■"
            boardRow10[2] = "■"
            boardRow10[3] = "■"
            boardRow10[4] = "■"
            boardRow10[5] = "■"
        elif carrier_spotH == 3:
            boardRow10[2] = "■"
            boardRow10[3] = "■"
            boardRow10[4] = "■"
            boardRow10[5] = "■"
            boardRow10[6] = "■"
        elif carrier_spotH == 4:
            boardRow10[3] = "■"
            boardRow10[4] = "■"
            boardRow10[5] = "■"
            boardRow10[6] = "■"
            boardRow10[7] = "■"        
        elif carrier_spotH == 5:
            boardRow10[4] = "■"
            boardRow10[5] = "■"
            boardRow10[6] = "■"
            boardRow10[7] = "■"
            boardRow10[8] = "■"   
        elif carrier_spotH == 6:
            boardRow10[5] = "■"
            boardRow10[6] = "■"
            boardRow10[7] = "■"
            boardRow10[8] = "■"
            boardRow10[9] = "■"
    
elif carrier_rotation == 2:
    if carrier_spotV == 1:
        if carrier_spotH == 1:
            boardRow1[0] = "■"
            boardRow2[0] = "■"
            boardRow3[0] = "■"
            boardRow4[0] = "■"
            boardRow5[0] = "■"
        elif carrier_spotH == 2:
            boardRow2[0] = "■"
            boardRow3[0] = "■"
            boardRow4[0] = "■"
            boardRow5[0] = "■"
            boardRow6[0] = "■"   
        elif carrier_spotH == 3:
            boardRow3[0] = "■"
            boardRow4[0] = "■"
            boardRow5[0] = "■"
            boardRow6[0] = "■"
            boardRow7[0] = "■"        
        elif carrier_spotH == 4:
            boardRow4[0] = "■"
            boardRow5[0] = "■"
            boardRow6[0] = "■"
            boardRow7[0] = "■"
            boardRow8[0] = "■"  
        elif carrier_spotH == 5:
            boardRow5[0] = "■"
            boardRow6[0] = "■"
            boardRow7[0] = "■"
            boardRow8[0] = "■"
            boardRow9[0] = "■" 
        elif carrier_spotH == 6:
            boardRow6[0] = "■"
            boardRow7[0] = "■"
            boardRow8[0] = "■"
            boardRow9[0] = "■"
            boardRow10[0] = "■"             
    elif carrier_spotV == 2:
        if carrier_spotH == 1:
            boardRow1[1] = "■"
            boardRow2[1] = "■"
            boardRow3[1] = "■"
            boardRow4[1] = "■"
            boardRow5[1] = "■"
        elif carrier_spotH == 2:
            boardRow2[1] = "■"
            boardRow3[1] = "■"
            boardRow4[1] = "■"
            boardRow5[1] = "■"
            boardRow6[1] = "■"   
        elif carrier_spotH == 3:
            boardRow3[1] = "■"
            boardRow4[1] = "■"
            boardRow5[1] = "■"
            boardRow6[1] = "■"
            boardRow7[1] = "■"        
        elif carrier_spotH == 4:
            boardRow4[1] = "■"
            boardRow5[1] = "■"
            boardRow6[1] = "■"
            boardRow7[1] = "■"
            boardRow8[1] = "■"  
        elif carrier_spotH == 5:
            boardRow5[1] = "■"
            boardRow6[1] = "■"
            boardRow7[1] = "■"
            boardRow8[1] = "■"
            boardRow9[1] = "■" 
        elif carrier_spotH == 6:
            boardRow6[1] = "■"
            boardRow7[1] = "■"
            boardRow8[1] = "■"
            boardRow9[1] = "■"
            boardRow10[1] = "■"
    elif carrier_spotV == 3:
        if carrier_spotH == 1:
            boardRow1[2] = "■"
            boardRow2[2] = "■"
            boardRow3[2] = "■"
            boardRow4[2] = "■"
            boardRow5[2] = "■"
        elif carrier_spotH == 2:
            boardRow2[2] = "■"
            boardRow3[2] = "■"
            boardRow4[2] = "■"
            boardRow5[2] = "■"
            boardRow6[2] = "■"   
        elif carrier_spotH == 3:
            boardRow3[2] = "■"
            boardRow4[2] = "■"
            boardRow5[2] = "■"
            boardRow6[2] = "■"
            boardRow7[2] = "■"        
        elif carrier_spotH == 4:
            boardRow4[2] = "■"
            boardRow5[2] = "■"
            boardRow6[2] = "■"
            boardRow7[2] = "■"
            boardRow8[2] = "■"  
        elif carrier_spotH == 5:
            boardRow5[2] = "■"
            boardRow6[2] = "■"
            boardRow7[2] = "■"
            boardRow8[2] = "■"
            boardRow9[2] = "■" 
        elif carrier_spotH == 6:
            boardRow6[2] = "■"
            boardRow7[2] = "■"
            boardRow8[2] = "■"
            boardRow9[2] = "■"
            boardRow10[2] = "■"
    elif carrier_spotV == 4:
        if carrier_spotH == 1:
            boardRow1[3] = "■"
            boardRow2[3] = "■"
            boardRow3[3] = "■"
            boardRow4[3] = "■"
            boardRow5[3] = "■"
        elif carrier_spotH == 2:
            boardRow2[3] = "■"
            boardRow3[3] = "■"
            boardRow4[3] = "■"
            boardRow5[3] = "■"
            boardRow6[3] = "■"   
        elif carrier_spotH == 3:
            boardRow3[3] = "■"
            boardRow4[3] = "■"
            boardRow5[3] = "■"
            boardRow6[3] = "■"
            boardRow7[3] = "■"        
        elif carrier_spotH == 4:
            boardRow4[3] = "■"
            boardRow5[3] = "■"
            boardRow6[3] = "■"
            boardRow7[3] = "■"
            boardRow8[3] = "■"  
        elif carrier_spotH == 5:
            boardRow5[3] = "■"
            boardRow6[3] = "■"
            boardRow7[3] = "■"
            boardRow8[3] = "■"
            boardRow9[3] = "■" 
        elif carrier_spotH == 6:
            boardRow6[3] = "■"
            boardRow7[3] = "■"
            boardRow8[3] = "■"
            boardRow9[3] = "■"
            boardRow10[3] = "■"
    elif carrier_spotV == 5:
        if carrier_spotH == 1:
            boardRow1[4] = "■"
            boardRow2[4] = "■"
            boardRow3[4] = "■"
            boardRow4[4] = "■"
            boardRow5[4] = "■"
        elif carrier_spotH == 2:
            boardRow2[4] = "■"
            boardRow3[4] = "■"
            boardRow4[4] = "■"
            boardRow5[4] = "■"
            boardRow6[4] = "■"   
        elif carrier_spotH == 3:
            boardRow3[4] = "■"
            boardRow4[4] = "■"
            boardRow5[4] = "■"
            boardRow6[4] = "■"
            boardRow7[4] = "■"        
        elif carrier_spotH == 4:
            boardRow4[4] = "■"
            boardRow5[4] = "■"
            boardRow6[4] = "■"
            boardRow7[4] = "■"
            boardRow8[4] = "■"  
        elif carrier_spotH == 5:
            boardRow5[4] = "■"
            boardRow6[4] = "■"
            boardRow7[4] = "■"
            boardRow8[4] = "■"
            boardRow9[4] = "■" 
        elif carrier_spotH == 6:
            boardRow6[4] = "■"
            boardRow7[4] = "■"
            boardRow8[4] = "■"
            boardRow9[4] = "■"
            boardRow10[4] = "■"
    elif carrier_spotV == 6:
        if carrier_spotH == 1:
            boardRow1[5] = "■"
            boardRow2[5] = "■"
            boardRow3[5] = "■"
            boardRow4[5] = "■"
            boardRow5[5] = "■"
        elif carrier_spotH == 2:
            boardRow2[5] = "■"
            boardRow3[5] = "■"
            boardRow4[5] = "■"
            boardRow5[5] = "■"
            boardRow6[5] = "■"   
        elif carrier_spotH == 3:
            boardRow3[5] = "■"
            boardRow4[5] = "■"
            boardRow5[5] = "■"
            boardRow6[5] = "■"
            boardRow7[5] = "■"        
        elif carrier_spotH == 4:
            boardRow4[5] = "■"
            boardRow5[5] = "■"
            boardRow6[5] = "■"
            boardRow7[5] = "■"
            boardRow8[5] = "■"  
        elif carrier_spotH == 5:
            boardRow5[5] = "■"
            boardRow6[5] = "■"
            boardRow7[5] = "■"
            boardRow8[5] = "■"
            boardRow9[5] = "■" 
        elif carrier_spotH == 6:
            boardRow6[5] = "■"
            boardRow7[5] = "■"
            boardRow8[5] = "■"
            boardRow9[5] = "■"
            boardRow10[5] = "■"
    elif carrier_spotV == 7:
        if carrier_spotH == 1:
            boardRow1[6] = "■"
            boardRow2[6] = "■"
            boardRow3[6] = "■"
            boardRow4[6] = "■"
            boardRow5[6] = "■"
        elif carrier_spotH == 2:
            boardRow2[6] = "■"
            boardRow3[6] = "■"
            boardRow4[6] = "■"
            boardRow5[6] = "■"
            boardRow6[6] = "■"   
        elif carrier_spotH == 3:
            boardRow3[6] = "■"
            boardRow4[6] = "■"
            boardRow5[6] = "■"
            boardRow6[6] = "■"
            boardRow7[6] = "■"        
        elif carrier_spotH == 4:
            boardRow4[6] = "■"
            boardRow5[6] = "■"
            boardRow6[6] = "■"
            boardRow7[6] = "■"
            boardRow8[6] = "■"  
        elif carrier_spotH == 5:
            boardRow5[6] = "■"
            boardRow6[6] = "■"
            boardRow7[6] = "■"
            boardRow8[6] = "■"
            boardRow9[6] = "■" 
        elif carrier_spotH == 6:
            boardRow6[6] = "■"
            boardRow7[6] = "■"
            boardRow8[6] = "■"
            boardRow9[6] = "■"
            boardRow10[6] = "■"
    elif carrier_spotV == 8:
        if carrier_spotH == 1:
            boardRow1[7] = "■"
            boardRow2[7] = "■"
            boardRow3[7] = "■"
            boardRow4[7] = "■"
            boardRow5[7] = "■"
        elif carrier_spotH == 2:
            boardRow2[7] = "■"
            boardRow3[7] = "■"
            boardRow4[7] = "■"
            boardRow5[7] = "■"
            boardRow6[7] = "■"   
        elif carrier_spotH == 3:
            boardRow3[7] = "■"
            boardRow4[7] = "■"
            boardRow5[7] = "■"
            boardRow6[7] = "■"
            boardRow7[7] = "■"        
        elif carrier_spotH == 4:
            boardRow4[7] = "■"
            boardRow5[7] = "■"
            boardRow6[7] = "■"
            boardRow7[7] = "■"
            boardRow8[7] = "■"  
        elif carrier_spotH == 5:
            boardRow5[7] = "■"
            boardRow6[7] = "■"
            boardRow7[7] = "■"
            boardRow8[7] = "■"
            boardRow9[7] = "■" 
        elif carrier_spotH == 6:
            boardRow6[7] = "■"
            boardRow7[7] = "■"
            boardRow8[7] = "■"
            boardRow9[7] = "■"
            boardRow10[7] = "■"
    elif carrier_spotV == 9:
        if carrier_spotH == 1:
            boardRow1[8] = "■"
            boardRow2[8] = "■"
            boardRow3[8] = "■"
            boardRow4[8] = "■"
            boardRow5[8] = "■"
        elif carrier_spotH == 2:
            boardRow2[8] = "■"
            boardRow3[8] = "■"
            boardRow4[8] = "■"
            boardRow5[8] = "■"
            boardRow6[8] = "■"   
        elif carrier_spotH == 3:
            boardRow3[8] = "■"
            boardRow4[8] = "■"
            boardRow5[8] = "■"
            boardRow6[8] = "■"
            boardRow7[8] = "■"        
        elif carrier_spotH == 4:
            boardRow4[8] = "■"
            boardRow5[8] = "■"
            boardRow6[8] = "■"
            boardRow7[8] = "■"
            boardRow8[8] = "■"  
        elif carrier_spotH == 5:
            boardRow5[8] = "■"
            boardRow6[8] = "■"
            boardRow7[8] = "■"
            boardRow8[8] = "■"
            boardRow9[8] = "■" 
        elif carrier_spotH == 6:
            boardRow6[8] = "■"
            boardRow7[8] = "■"
            boardRow8[8] = "■"
            boardRow9[8] = "■"
            boardRow10[8] = "■"
    elif carrier_spotV == 10:
        if carrier_spotH == 1:
            boardRow1[9] = "■"
            boardRow2[9] = "■"
            boardRow3[9] = "■"
            boardRow4[9] = "■"
            boardRow5[9] = "■"
        elif carrier_spotH == 2:
            boardRow2[9] = "■"
            boardRow3[9] = "■"
            boardRow4[9] = "■"
            boardRow5[9] = "■"
            boardRow6[9] = "■"   
        elif carrier_spotH == 3:
            boardRow3[9] = "■"
            boardRow4[9] = "■"
            boardRow5[9] = "■"
            boardRow6[9] = "■"
            boardRow7[9] = "■"        
        elif carrier_spotH == 4:
            boardRow4[9] = "■"
            boardRow5[9] = "■"
            boardRow6[9] = "■"
            boardRow7[9] = "■"
            boardRow8[9] = "■"  
        elif carrier_spotH == 5:
            boardRow5[9] = "■"
            boardRow6[9] = "■"
            boardRow7[9] = "■"
            boardRow8[9] = "■"
            boardRow9[9] = "■" 
        elif carrier_spotH == 6:
            boardRow6[9] = "■"
            boardRow7[9] = "■"
            boardRow8[9] = "■"
            boardRow9[9] = "■"
            boardRow10[9] = "■"
 
           
            
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
