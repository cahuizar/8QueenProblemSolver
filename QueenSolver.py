import random
from pprint import pprint

random.seed(5)

class QueenSolver:
    def __init__(self):
        self.queens = [-9,-9,-9,-9,-9,-9,-9,-9]
        self.no_conflict = 0
        self.isFinalState = False
        self.column_conflict = [-9,-9,-9,-9,-9,-9,-9,-9]
        self.movesCounter = 0

    def showQueens(self):
        pprint(self.queens)
        print '\n'

    def Search(self):
        column = 7
        self.same_col = False
        self.no_change = 0
        while(self.isFinalState == False):
            # iterate through rows in columns
            for row in range(0, 8):
                self.column_conflict[row] = self.ConflictCount(row, column)
            # store the current queen position 
            cur_queen_position = self.queens[column]
            # pick a random row that has min conflict
            self.queens[column] = self.RowPicker(self.column_conflict)
            # do not increment queen move counter if the queen did not move
            if(cur_queen_position == self.queens[column]):
                self.same_col = True
                self.no_change += 1
            else:
                print 'Queen from column '+str(column)+' has been moved from '+str(cur_queen_position)+' to '+str(self.queens[column])
                self.movesCounter += 1
            # loop back 
            if(column == 0):
                column = 7
            else:
                column -= 1
            #check for final state
            self.isFinalState = self.InFinalState()
                
    def InFinalState(self):
        # final state if there are no more conflicts or if queen position does not change
        if(self.no_conflict == 8 or self.no_change == 20):
            print 'Final queen moves: '+str(self.movesCounter)
            print "Final State list: "
            self.showQueens()
            return True
        # display queen array after a change of row occurs
        elif(self.same_col == False):
            print 'Queen moves: '+str(self.movesCounter)
            print "New Queen list: "
            self.showQueens()
            self.no_change = 0
        else:
            self.same_col = False
        return False
        
    def ConflictCount(self, row, column):
        conflict = 0
        conflict = self.SouthEastConflict(row, column, conflict)
        conflict = self.EastConflict(row, column, conflict)
        conflict = self.NorthEastConflict(row, column, conflict)
        conflict = self.NorthWestConflict(row, column, conflict)
        conflict = self.WestConflict(row, column, conflict)
        conflict = self.SouthWestConflict(row, column, conflict)
        return conflict

    # compute the min conflict for each column when initializing     
    def Initialization(self):
        for column in range(0,8):
            for row in range(0, 8):
                self.column_conflict[row] = self.InitConflict(row, column)
            self.queens[column] = self.RowPicker(self.column_conflict)
        print 'Initialized Queens:'
        self.showQueens()

    # choose a random row based on the minimum conflict
    def RowPicker(self, column_conflict):
        random_pick = 0
        min_value = self.column_conflict[0]
        temp_min_conflict = [0]
        for x in range(1,8):
            # reset the values on temp array if a new min conflict was found
            if(min_value > column_conflict[x]):
                temp_min_conflict[:] = []
                min_value = self.column_conflict[x]
                temp_min_conflict.append(x)
            # store the min row index when # of conflicts are of equal value
            elif(min_value == self.column_conflict[x]):
                temp_min_conflict.append(x)
        # if the min conflict value is 0 then increment the no conflict counter
        if(min_value == 0):
            self.no_conflict += 1
        # reset the counter if the min value is greater than 1
        else:
            self.no_conflict = 0
        random_pick = self.RandomPicker(temp_min_conflict)
        return random_pick

    # pick a random value in the list depending on the random seed specified 
    def RandomPicker(self, temp_min_conflict):
        return random.choice(temp_min_conflict)
        
    def InitConflict(self, row, column):
        conflict = 0
        conflict = self.NorthWestConflict(row, column, conflict)
        conflict = self.WestConflict(row, column, conflict)
        conflict = self.SouthWestConflict(row, column, conflict)
        return conflict
    
    # The following methods will calculate the conflict to its on corresponding direction
    
    def NorthWestConflict(self, row, column, conflict):
        index_counter = row
        column_counter = column
        while(index_counter != 0 and column_counter !=0):
            index_counter -= 1
            column_counter -= 1
            if( index_counter == self.queens[column_counter]):
                conflict += 1
        return conflict

    def WestConflict(self, row, column, conflict):
        while(column != 0):
            column -= 1
            if(self.queens[column] == row):
                conflict += 1
        return conflict        

    def SouthWestConflict(self, row, column, conflict):
        while(column != 0 and row != 7):
            row += 1
            column -= 1
            if( row == self.queens[column]):
                conflict += 1
        return conflict

    def SouthEastConflict(self, row, column, conflict):
        while(row != 7 and column != 7):
            row += 1
            column += 1
            if(row == self.queens[column]):
                conflict += 1
        return conflict

    def EastConflict(self, row, column, conflict):
        while(column != 7):
            column += 1
            if(self.queens[column] == row):
                conflict += 1
        return conflict

    def NorthEastConflict(self, row, column, conflict):
        while(row != 0 and column != 7):
            row -= 1
            column += 1
            if( row == self.queens[column]):
                conflict += 1
        return conflict
