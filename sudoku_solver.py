class Game():
    sudoku_array = [] # [ [value of zero, [sudoku_array]], [],... ]
    zeros_array = [] # [ [(coords), [values to avoid]], [],... ]

    def __init__(self, game_n):
        self.game_n = game_n
        Game.sudoku_array.append([0,game_n[0]])


    def solve(self):

        found_zero = False
        last_array = Game.sudoku_array[len(Game.sudoku_array)-1][1]
        coords = ()
        green = True

        for row in last_array:
            for value in row:
                if value == 0:
                    if not found_zero:

                        # Saves coordinates of zero
                        x = row.index(value)
                        y = last_array.index(row)

                        coords = (x,y)

                        # Saves zero coordinates if wasn't there yet
                        coordinates = []
                        for i in range(len(Game.zeros_array)):
                            coordinates.append(Game.zeros_array[i][0])

                        done = False
                        for i in coordinates:
                            if (not (x,y) in coordinates) and not done:
                                Game.zeros_array.append([(x,y),[0]])
                                done = True

                        if len(Game.zeros_array) == 0:
                            Game.zeros_array.append([(x,y),[0]])          

                        # Boolean to see if it can find a value: if it does then it gets a value, if not it tries the previous zero
                        (found_value, value_of_0) = Game.position_0()             

                        #add to 'values to avoid' of last value of last zero and pops current zero
                        if not found_value:
                            green = False
                            # 'value of zero' from sudoku_array --> passes to --> 'values to avoid' from zeros_array
                            Game.zeros_array[len(Game.zeros_array)-1-1][1].append(Game.sudoku_array[len(Game.sudoku_array)-1][0])

                            # Put a zero on the value where didn't found any more values
                            change_value = Game.zeros_array[len(Game.zeros_array)-1-1][0]
                            for index, row in enumerate(Game.sudoku_array[len(Game.sudoku_array)-1][1]):
                                if index == change_value[1]:
                                    for index2, value2 in enumerate(row):
                                        if index2 == change_value[0]:
                                            Game.sudoku_array[len(Game.sudoku_array)-1][1][index].pop(index2)
                                            Game.sudoku_array[len(Game.sudoku_array)-1][1][index].insert(index2,0)

                            # Pops last of sudoku_array
                            Game.sudoku_array.pop()
                            Game.zeros_array.pop()

                        # Create new array and change value of the zero
                        if found_value:
                            already_done = False
                            new_sudoku = Game.sudoku_array[len(Game.sudoku_array)-1][1].copy()
                            for index2, row2 in enumerate(Game.sudoku_array[len(Game.sudoku_array)-1][1]):
                                for index, value2 in enumerate(row2):
                                    if value2 == 0 and not already_done:
                                        new_sudoku[index2].pop(index)
                                        new_sudoku[index2].insert(index,value_of_0)
                                        already_done = True

                            Game.sudoku_array.append([value_of_0, new_sudoku])
                        
                    found_zero = True
        return (coords,green)

        

    # Checks if found all values (no zeros left)
    @classmethod
    def check_zero(cls):
        found_zero = False
        for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
            for value in row:
                if value == 0:
                    found_zero = True
        return found_zero
                        

    # Here goes the conditions/rules of sudoku   
    @classmethod                    
    def position_0(cls):
        found_value = False
        value_of_0 = 0
        possible_n = [r for r in range(1,10)]
        available_row = []
        available_col = []
        available_box = []
        available = []

        # Get coords from last zero from zeros_array
        x = 9
        y = 9
        index02 = 0
        for i in Game.zeros_array:
            if not i[1] == []:  
                index02 = Game.zeros_array.index(i)
                (x,y) = Game.zeros_array[index02][0]
        
        # Get values to avoid
        values_to_avoid = Game.zeros_array[index02][1]

        # Get row
        row = []
        for row2 in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
            row_index = Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row2)
            if row_index == y:
                row = row2
        
        # Get column
        col = []
        for row3 in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
            for index, value3 in enumerate(row3):
                if index == x:
                    col.append(value3)

        # Get box
        box = Game.get_box(x,y)

        # Get posible numbers from, row, column and box (see values to avoid to)
        available_row = possible_n.copy()
        for i in range(1,10):
            if i in row:
                available_row.remove(i)

        available_col = possible_n.copy()
        for i in range(1,10):
            if i in col:
                available_col.remove(i)

        available_box = possible_n.copy()
        for i in range(1,10):
            if i in box:
                available_box.remove(i)

            #If none: found_value = False

            #If multiple: do the lowest first: value_of_0 = lowest
        
        for i in range(1,10):
            if i in available_row and i in available_col and i in available_box and i not in values_to_avoid:
                available.append(i)
                found_value  = True

        available.sort()

        try:
            value_of_0 = available[0]
        except:
            value_of_0 = 0

        return (found_value, value_of_0)
        
    @staticmethod
    def get_box(x,y):
        box = []
        box_1 = [
            (0, 0), (1, 0), (2, 0), 
            (0, 1), (1, 1), (2, 1), 
            (0, 2), (1, 2), (2, 2)
        ]
        box_2 = [
            (3, 0), (4, 0), (5, 0),
            (3, 1), (4, 1), (5, 1),
            (3, 2), (4, 2), (5, 2)
        ]
        box_3 = [
            (6, 0), (7, 0), (8, 0),
            (6, 1), (7, 1), (8, 1),
            (6, 2), (7, 2), (8, 2)
        ]
        box_4 = [
            (0, 3), (1, 3), (2, 3),
            (0, 4), (1, 4), (2, 4),
            (0, 5), (1, 5), (2, 5)
        ]
        box_5 = [
            (3, 3), (4, 3), (5, 3),
            (3, 4), (4, 4), (5, 4),
            (3, 5), (4, 5), (5, 5)
        ]
        box_6 = [
            (6, 3), (7, 3), (8, 3),
            (6, 4), (7, 4), (8, 4),
            (6, 5), (7, 5), (8, 5)
        ]
        box_7 = [
            (0, 6), (1, 6), (2, 6),
            (0, 7), (1, 7), (2, 7),
            (0, 8), (1, 8), (2, 8)
        ]
        box_8 = [
            (3, 6), (4, 6), (5, 6),
            (3, 7), (4, 7), (5, 7),
            (3, 8), (4, 8), (5, 8)
        ]
        box_9 = [
            (6, 6), (7, 6), (8, 6),
            (6, 7), (7, 7), (8, 7),
            (6, 8), (7, 8), (8, 8)
        ]

        if (x,y) in box_1:
            for coords in box_1:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        elif (x,y) in box_2:
            for coords in box_2:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        elif (x,y) in box_3:
            for coords in box_3:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        elif (x,y) in box_4:
            for coords in box_4:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        elif (x,y) in box_5:
            for coords in box_5:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        elif (x,y) in box_6:
            for coords in box_6:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)
                                
        elif (x,y) in box_7:
            for coords in box_7:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        elif (x,y) in box_8:
            for coords in box_8:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        else:
            for coords in box_9:
                (u,w) = coords
                for row in Game.sudoku_array[len(Game.sudoku_array)-1][1]:
                    if Game.sudoku_array[len(Game.sudoku_array)-1][1].index(row) == w:
                        for index, value in enumerate(row):
                            if index == u:
                                box.append(value)

        return box

    @classmethod
    def display(cls):
        last_array = Game.sudoku_array[len(Game.sudoku_array)-1][1]
        for row in last_array:
            print(row)


# Run the file only (this part will not work if this file is imported from another one)
if __name__ == "__main__":
    # Game3 
    preset3 = [
        [2,0,0,9,0,4,6,0,0],
        [0,0,0,0,6,0,1,0,3],
        [0,0,9,0,0,3,0,0,0],
        [0,0,0,0,0,2,0,7,5],
        [0,0,5,0,0,0,2,0,0],
        [1,9,0,4,0,0,0,0,0],
        [0,0,0,6,0,0,5,0,0],
        [8,0,4,0,2,0,0,0,0],
        [0,0,3,7,0,8,0,0,2]
    ]

    solution3 = [
        [2,3,1,9,8,4,6,5,7],
        [5,4,8,2,6,7,1,9,3],
        [7,6,9,5,1,3,8,2,4],
        [3,8,6,1,9,2,4,7,5],
        [4,7,5,8,3,6,2,1,9],
        [1,9,2,4,7,5,3,8,6],
        [9,2,7,6,4,1,5,3,8],
        [8,5,4,3,2,9,7,6,1],
        [6,1,3,7,5,8,9,4,2]
    ]
    game3 = [preset3, solution3]

    sudoku = Game(game3)
    while sudoku.check_zero():
        sudoku.solve()
    sudoku.display()

    last_array = Game.sudoku_array[len(Game.sudoku_array)-1][1]
    print(game3[1] == last_array)
