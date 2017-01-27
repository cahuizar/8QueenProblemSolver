test = [7,7,6,7,0,3,0,4]

conflict = 0;

def main():
    SouthWest(5);
    print(conflict);

def NorthWestConflict(cur_index):
    global conflict
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

def West(cur_index):
    global conflict
    print("Searching for conflicts on West")
    conflict = 0;
    index_counter = cur_index
    while(index_counter != 0):
        print("Index_counter: ",index_counter)
        index_counter -= 1
        if(test[cur_index] == test[index_counter]):
            print("Same on column: ",index_counter)
            conflict += 1
        

def SouthWest(cur_index):
    global conflict
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
            
    

main();
