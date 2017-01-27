test = [7,0,3,7,0,3,0,4]

#expects 1
def main():
    conflict = West(3);
    print(conflict);

def NorthWestConflict(cur_index):
    print("Testing NorthWestConflict")
    conflict = 0;
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

def West(cur_index):
    print("Testing West")
    conflict = 0;
    index_counter = cur_index
    while(index_counter != 0):
        print("Index_counter: ",index_counter)
        index_counter -= 1
        if(test[cur_index] == test[index_counter]):
            print("Same on column: ",index_counter)
            conflict += 1
            
    return conflict
            
    

main();
