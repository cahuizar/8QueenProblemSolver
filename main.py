test = [7,7,2,6,5,3,6,1]

queens = []

conflict = 0;

#create conflict function

def main():
    Initialize()

def Initialize()
    column_conflict = []
    row = 0;
    #for(int row =0; row < 8; row++):
    column_conflict[row] = InitConflict(row)
        
def InitConflict(row)
    conflict = 0
    conflict = NorthWest(row, conflict)
    conflict = West(row, conflict)
    conflict = SouthWest(row, conflict)
    return conflict    
    
def NorthWestConflict(cur_index, conflict):
    print("Searching for conflicts on NorthWestConflict")
    index_counter = cur_index
    column_value = test[cur_index]
    while(index_counter != 0 and column_value != 0):
        index_counter -= 1
        column_value -= 1
        print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            print("Actual Column value: ",column_value)
            print("Col val: ",test[index_counter])
            conflict += 1
    return conflict

def WestConflict(cur_index, conflict):
    print("Searching for conflicts on West")
    conflict = 0;
    index_counter = cur_index
    while(index_counter != 0):
        print("Index_counter: ",index_counter)
        index_counter -= 1
        if(test[cur_index] == test[index_counter]):
            print("Same on column: ",index_counter)
            conflict += 1
    return conflict
        

def SouthWestConflict(cur_index, conflict):
    print("Searching for conflicts on SouthWest")
    index_counter = cur_index
    column_value = test[cur_index]
    while(index_counter != 0 and column_value != 7):
        index_counter -= 1
        column_value += 1
        print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            print("Actual Column value: ",column_value)
            print("Col val: ",test[index_counter])
            conflict += 1
    return conflict

def SouthEastConflict(cur_index, conflict):
    print("Searching for conflicts on SouthEast")
    index_counter = cur_index
    column_value = test[cur_index]
    while(index_counter != 7 and column_value != 7):
        index_counter += 1
        column_value += 1
        print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            print("Actual Column value: ",column_value)
            print("Col val: ",test[index_counter])
            conflict += 1
    return conflict

def EastConflict(cur_index, conflict):
    print("Searching for conflicts on East")
    conflict = 0;
    index_counter = cur_index
    while(index_counter != 7):
        print("Index_counter: ",index_counter)
        index_counter += 1
        if(test[cur_index] == test[index_counter]):
            print("Same on column: ",index_counter)
            conflict += 1
    return conflict

def NorthEastConflict(cur_index, conflict):
    global conflict
    print("Searching for conflicts on NorthEastConflict")
    index_counter = cur_index
    column_value = test[cur_index]
    while(index_counter != 7 and column_value != 0):
        index_counter += 1
        column_value -= 1
        print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            print("Actual Column value: ",column_value)
            print("Col val: ",test[index_counter])
            conflict += 1
    return conflict

main();
