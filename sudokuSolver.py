import math

def squareCheck(sudoku,i,j,k):
    base = int(math.sqrt(len(sudoku)))
    rowStart = i - i%base
    #print(rowStart)
    colStart = j - j%base
    #print(colStart)
    for row in range(rowStart,rowStart+3):
        #print(f"row {row}",end=" ")
        for col in range(colStart,colStart+3):
            #print(f"row {row} col {col}","'",sudoku[row][col],"'",end=" ")
            if k == sudoku[row][col]:
                return True
        #print(" ")
    return False

def colCheck(sudoku,i,k):
    for c in range(len(sudoku)):
        if k == sudoku[i][c]:
            return True
    return False

def rowCheck(sudoku,j,k):
    for c in range(len(sudoku)):
        if k == sudoku[c][j] :
            return True
    return False

def Check(sudoku,i,j,k):
    if rowCheck(sudoku,j,k):
        return False
    elif colCheck(sudoku,i,k):
        return False
    elif squareCheck(sudoku,i,j,k):
        return False
    else:
        return True

def sudokusolver(sudoku):
    t = True
    for i,v in enumerate(sudoku):
        for j,va in enumerate(v):
            if va == 0:
                t = False
                break
        if t:
            pass
        else:
            break

    if t:
        return True
    for k in range(1,len(sudoku)+1):
        if Check(sudoku,i,j,k):
            sudoku[i][j] = k
            if sudokusolver(sudoku):
                return True
            else:
                sudoku[i][j] = 0
    
    return False

def display(sudoku):
    l=1
    m=1
    for i in sudoku:
        if l%3 == 0:
            for j in i:
                if m%3==0:
                    print(j,end="|")
                    m = m + 1
                else:
                    print(j,end=" ")
                    m = m + 1
            print("")
            for k in range(len(sudoku)):
                    print(end="__")

        else:
            for j in i:
                if m%3==0:
                    print(j,end="|")
                    m = m + 1                    
                else:
                    print(j,end=" ")
                    m = m + 1
        l=l+1
        m = 1
        print(" ")

def main():
    # first sudoku space or matrix
    sudoku = [
        [8,0,1,0,0,3,9,0,6],
        [0,0,9,0,0,7,8,5,0],
        [2,5,0,1,0,0,4,7,0],
        [5,0,0,0,6,1,7,0,4],
        [7,6,0,8,3,0,0,0,0],
        [0,3,2,0,0,0,0,0,0],
        [0,2,0,0,1,9,5,0,0],
        [0,0,5,0,0,0,3,0,2],
        [0,0,0,4,5,2,1,9,7]
    ]
    # sudoku matrix is fine
    #print(len(sudoku))
    display(sudoku)
    print("!!! SOLVE !!!")
    if sudokusolver(sudoku):
        display(sudoku)
    else:
        print("sudoku don't have the solution")

if __name__ == "__main__":
    main()