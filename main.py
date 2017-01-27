test = [4,1,3,7,4,3,6,4]

#expects 1
def main():
    conflict = NorthWestConflict(6);
    print(conflict);

def NorthWestConflict(cur_index):
    conflict = 0;
    index_counter = cur_index
    column_value = test[cur_index]
    while(index_counter != 0 and column_value != 0):
        index_counter = index_counter - 1
        column_value = column_value - 1
        print("Index_counter: ",index_counter)
        if( column_value == test[index_counter]):
            print("Actual Column value: ",column_value)
            print("Col val: ",test[index_counter])
            conflict= conflict + 1

    return conflict
    

main();
