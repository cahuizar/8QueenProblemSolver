test = [0,1,2,3,4,5,6,7]

#expects 3
def main():
    conflict = NorthWestConflict(4);
    print(conflict);

def NorthWestConflict(cur_index):
    conflict = 0;
    index_counter = cur_index
    while(index_counter != 0):
        print("Index_counter: ",index_counter)
        index_counter = index_counter - 1
        if(test[cur_index] == test[index_counter]):
            conflict= conflict + 1

    return conflict
    

main();
