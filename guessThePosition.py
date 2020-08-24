import random

class coordinate():
    def __init__(self,row,col):
        self.row = row
        self.col = col

def display(space,s):
    for i in range(len(space)):
        if(s.row == i):
            for j in range(len(space)):
                if(j == s.col):
                    space[i][j] = "#"
                    print(space[i][j],end=" ")
                else:
                    print(space[i][j],end=" ")
        else:
            for j in range(len(space)):
                print(space[i][j],end=" ")

        print(" ")
    return space

def coordinateRepeatCheckcomputer(spaceUsed,row,col):
    for i in spaceUsed:
        if(row == i.row and col == i.col):
            rowAgain = random.randint(0,2)
            colAgain = random.randint(0,2)
            s = coordinate(rowAgain,colAgain)
            spaceUsed,s = coordinateRepeatCheckcomputer(spaceUsed,s.row,s.col)
            return spaceUsed,s
    s = coordinate(row,col)
    spaceUsed.append(s)
    return spaceUsed,s
    
def coordinateRepeatCheck(spaceUsed,row,col):
    if (len(spaceUsed) == 0):
        s = coordinate(row,col)
        spaceUsed.append(s)
        return spaceUsed,s
    else:
        for i in spaceUsed:
            if(row == i.row and col == i.col):
                print(i.row+1 ," and ",i.col+1 ," already used enter another coordinate : ")
                rowAgain = int(input("Enter the row : "))
                colAgain = int(input("Enter the col : "))
                s = coordinate(rowAgain-1,colAgain-1)
                spaceUsed,s = coordinateRepeatCheck(spaceUsed,s.row,s.col)
                return spaceUsed,s
        s = coordinate(row,col)
        spaceUsed.append(s)
        return spaceUsed,s
        
def catchCoordinate(point,cc,SecretCoordinate):
    for i in SecretCoordinate:
        if cc.row == i.row and cc.col == i.col:
            print(f"You catch the point is {i.row+1} and {i.col+1}")
            #spaceUsed.append(cc)
            point = point + 1
    return point


def main():
    name = input("Enter the name : ")
    #Name = name.capitalize()
    diagonalOfSpace = int(input("Enter matrix diagonal : "))
    space = [["*" for i in range(diagonalOfSpace)]for j in range(diagonalOfSpace)]
    print("The number attempt is equal to diagonal of matrix that is :",diagonalOfSpace)
    spaceUsed = []
    userSecretCoordinate = []
    computerSecretCoordinate = []
    print(f"{name} Enter the point")
    while True:
        for i in range(diagonalOfSpace): # for user for input
            row = int(input("Enter row index : "))
            row = row - 1
            col = int(input("Enter the column index : "))
            col = col - 1
            spaceUsed,s = coordinateRepeatCheck(spaceUsed,row,col)
            space = display(space,s)
            userSecretCoordinate.append(s)
            print("The ",(i+1)," position is filled ")

        print("The computer term start")
        for i in range(diagonalOfSpace): # for computer input by random
            row = random.randint(0,2)
            col = random.randint(0,2)
            spaceUsed,s = coordinateRepeatCheckcomputer(spaceUsed, row,col)
            #space = display(space,s)
            computerSecretCoordinate.append(s)
            print("The ",(i+1)," position is filled ")
        
        break
    print("### GAME START ###")
    print("Who guess the opponent position first will win\nENJOY!")
    userPoint = 0
    computerPoint = 0
    while True:
        print(f"-- {name.capitalize()} ENTER THE COORDINATE --")
        row = int(input("Enter the row coordinate : "))
        row = row -1
        col = int(input("Enter the col coordinate : "))
        col = col - 1
        cc = coordinate(row,col)
        userPoint = catchCoordinate(userPoint,cc,computerSecretCoordinate)
        print(f"{name} point : {userPoint}")
        space = display(space,cc)
        if userPoint == 3:
            break

        print("-- COMPUTER ENTER THE COORDINATE --")
        crow = random.randint(0,2)
        ccol = random.randint(0,2)
        ccc = coordinate(crow,ccol)
        computerSecretCoordinate,ccc = coordinateRepeatCheckcomputer(computerSecretCoordinate,ccc.row,ccc.col)
        computerPoint= catchCoordinate(computerPoint,ccc,userSecretCoordinate)
        #space = display(space,ccc)
        print(f"computer point : {computerPoint}")
        print("-- COMPUTER ENTERED THE COORDINATE --")
        if computerPoint == 3:
            break
    
    if userPoint == diagonalOfSpace:
        print(f"{name} won the game ")
    else:
        print("computer won the game ")

    print("!! END !!")
    

if __name__ == "__main__":
    main()