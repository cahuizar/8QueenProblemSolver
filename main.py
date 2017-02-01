import random
from pprint import pprint

random.seed(5)

def main():
    global queens
    global no_conflict
    no_conflict = 0
    queens = [-9,-9,-9,-9,-9,-9,-9,-9]
    Initialize()
    Search()

def showQueens():
    global queens
    pprint(queens)

def Search():
    global no_conflict
    global queens
    isFinalState = False
    column = 7
    column_conflict = [-9,-9,-9,-9,-9,-9,-9,-9]
    while(isFinalState == False):
        for row in range(0, 8):
            column_conflict[row] = ConflictCount(row, column)
        queens[column] = RowPicker(column_conflict)
        if(column == 0):
            column = 7
        else:
            column -= 1
        isFinalState = InFinalState()
            
def InFinalState():
    if(no_conflict == 8):
        print "Solution: "
        showQueens()
        return True
    return False
    
def ConflictCount(row, column):
    conflict = 0
    conflict = SouthEastConflict(row, column, conflict)
    conflict = EastConflict(row, column, conflict)
    conflict = NorthEastConflict(row, column, conflict)
    conflict = NorthWestConflict(row, column, conflict)
    conflict = WestConflict(row, column, conflict)
    conflict = SouthWestConflict(row, column, conflict)
    return conflict
    
def Initialize():
    global queens
    column_conflict = [-9,-9,-9,-9,-9,-9,-9,-9]
    for column in range(0,8):
        for row in range(0, 8):
            column_conflict[row] = InitConflict(row, column)
        queens[column] = RowPicker(column_conflict)
    print 'Initialized Queens:'
    showQueens()

def RowPicker(column_conflict):
    global no_conflict
    random_pick = 0
    min_value = column_conflict[0]
    temp_min_conflict = [0]
    for x in range(1,8):
        if(min_value > column_conflict[x]):
            temp_min_conflict[:] = []
            min_value = column_conflict[x]
            temp_min_conflict.append(x)
        elif(min_value == column_conflict[x]):
            temp_min_conflict.append(x)
    if(min_value == 0):
        no_conflict += 1
    else:
        no_conflict = 0
    random_pick = RandomPicker(temp_min_conflict)
    return random_pick
    
def RandomPicker(temp_min_conflict):
    return random.choice(temp_min_conflict)
    
def InitConflict(row, column):
    conflict = 0
    conflict = NorthWestConflict(row, column, conflict)
    conflict = WestConflict(row, column, conflict)
    conflict = SouthWestConflict(row, column, conflict)
    return conflict    
    
def NorthWestConflict(row, column, conflict):
    global queens
    index_counter = row
    column_counter = column
    while(index_counter != 0 and column_counter !=0):
        index_counter -= 1
        column_counter -= 1
        if( index_counter == queens[column_counter]):
            conflict += 1
    return conflict

def WestConflict(row, column, conflict):
    global queens
    while(column != 0):
        column -= 1
        if(queens[column] == row):
            conflict += 1
    return conflict        

def SouthWestConflict(row, column, conflict):
    global queens
    while(column != 0 and row != 7):
        row += 1
        column -= 1
        if( row == queens[column]):
            conflict += 1
    return conflict

def SouthEastConflict(row, column, conflict):
    global queens
    while(row != 7 and column != 7):
        row += 1
        column += 1
        if(row == queens[column]):
            conflict += 1
    return conflict

def EastConflict(row, column, conflict):
    global queens
    while(column != 7):
        column += 1
        if(queens[column] == row):
            conflict += 1
    return conflict

def NorthEastConflict(row, column, conflict):
    global queens
    while(row != 0 and column != 7):
        row -= 1
        column += 1
        if( row == queens[column]):
            conflict += 1
    return conflict

main();
