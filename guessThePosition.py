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

def coordinateRepeatCheck(spaceUsed,row,col):
    if (len(spaceUsed) == 0):
        s = coordinate(row,col)
        spaceUsed.append(s)
        return spaceUsed,s
    else:
        for i in spaceUsed:
            if(row == i.row and col == i.col):
                #print(i.row+1 ," and ",i.col+1 ," already used enter another coordinate : ")
                #rowAgain = int(input("Enter the row : "))
                rowAgain = random.randint(1,3)
                #colAgain = int(input("Enter the col : "))
                colAgain = random.randint(1,3)
                s = coordinate(rowAgain-1,colAgain-1)
                spaceUsed,s = coordinateRepeatCheck(spaceUsed,s.row,s.col)
                return spaceUsed,s
        s = coordinate(row,col)
        spaceUsed.append(s)
        return spaceUsed,s
        
def main():
    diagonalOfSpace = int(input("Enter matrix diagonal : "))
    space = [["*" for i in range(diagonalOfSpace)]for j in range(diagonalOfSpace)]
    spaceUsed = []
    i = 0
    while i != 5:
        #row = int(input("Enter row index : "))
        row = random.randint(1,3)
        row = row - 1
        #col = int(input("Enter the column index : "))
        col = random.randint(1,3)
        col = col - 1
        spaceUsed,s = coordinateRepeatCheck(spaceUsed, row,col)
        space = display(space,s)
        print(i+1," round end !! ")
        i  = i + 1
    
    print("!! END !!")
    

if __name__ == "__main__":
    main()