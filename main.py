import random

test = [7,7,2,6,5,3,6,1]



#create conflict function

def main():
    global queens
    queens = [-9,-9,-9,-9,-9,-9,-9,-9]
    Initialize()
    
def showQueens():
    global queens
    for x in range(0,8):
        print str(queens[x])
    
def Initialize():
    global queens
    column_conflict = [-9,-9,-9,-9,-9,-9,-9,-9]
    for column in range(0,8):
        for row in range(0, 8):
            column_conflict[row] = InitConflict(row, column)
            print "Conflict = "+ str(column_conflict[row]) +" for row "+ str(row)
        queens[column] = RowPicker(column_conflict)

        print "Queen in Column "+ str(column) +" is "+ str(queens[column])+ "\n"
        showQueens()

def RowPicker(column_conflict):
    random_pick = 0
    min_value = column_conflict[0]
    temp_min_conflict = [0]
    for y in range(len(column_conflict)):
        print column_conflict[y]
    for x in range(1,8):
        if(min_value > column_conflict[x]):
            temp_min_conflict[:] = []
            min_value = column_conflict[x]
            temp_min_conflict.append(x)
        elif(min_value == column_conflict[x]):
            temp_min_conflict.append(x)
    random_pick = RandomPicker(temp_min_conflict)
    return random_pick
    
def RandomPicker(temp_min_conflict):
    return random.choice(temp_min_conflict)
    
def InitConflict(row, column):
    conflict = 0
    conflict = NorthWestConflict(row, column, conflict)
    print(str(conflict))
    conflict = WestConflict(row, column, conflict)
    print(str(conflict))
    conflict = SouthWestConflict(row, column, conflict)
    print(str(conflict))
    return conflict    
    
def NorthWestConflict(row, column, conflict):
    global queens
    print("Searching for conflicts on NorthWestConflict")
    index_counter = row
    column_counter = column
    while(index_counter != 0 and column_counter !=0):
        index_counter -= 1
        column_counter -= 1
        print "Index counter = "+ str(index_counter) + " and queens is "+ str(queens[column_counter])
        #print("Index_counter: ",index_counter)
        if( index_counter == queens[column_counter]):
            print("Actual Column value: ",index_counter)
            print("Col val: ",queens[index_counter])
            conflict += 1
    return conflict

def WestConflict(row, column, conflict):
    global queens
    print("Searching for conflicts on West")
    while(column != 0):
        #print("Index_counter: ",index_counter)
        column -= 1
        print "Column: "+ str(column)
        print "Row: "+ str(row)
        print "Column = "+ str(column) + " and queens is "+ str(queens[row])
        if(queens[column] == row):
            #print("Same on column: ",index_counter)
            conflict += 1
    return conflict
        

def SouthWestConflict(row, column, conflict):
    global queens
    print("Searching for conflicts on SouthWest")
    while(column != 0 and row != 7):
        row += 1
        column -= 1
        if( row == queens[column]):
            #print("Actual Column value: ",column_value)
            #print("Col val: ",queens[index_counter])
            print "Conflict found"
            conflict += 1
    return conflict

def SouthEastConflict(row, conflict):
    global queens
    print("Searching for conflicts on SouthEast")
    index_counter = row
    column_value = test[row]
    while(index_counter != 7 and column_value != 7):
        index_counter += 1
        column_value += 1
        #print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            #print("Actual Column value: ",column_value)
            #print("Col val: ",test[index_counter])
            conflict += 1
    return conflict

def EastConflict(row, conflict):
    global queens
    print("Searching for conflicts on East")
    conflict = 0;
    index_counter = row
    while(index_counter != 7):
        #print("Index_counter: ",index_counter)
        index_counter += 1
        if(test[row] == test[index_counter]):
            #print("Same on column: ",index_counter)
            conflict += 1
    return conflict

def NorthEastConflict(row, conflict):
    global queens
    print("Searching for conflicts on NorthEastConflict")
    index_counter = row
    column_value = test[row]
    while(index_counter != 7 and column_value != 0):
        index_counter += 1
        column_value -= 1
        #print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            #print("Actual Column value: ",column_value)
            #print("Col val: ",test[index_counter])
            conflict += 1
    return conflict

main();
