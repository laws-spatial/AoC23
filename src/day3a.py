# imports
from pathlib import Path
import numpy as np

# read data
data_folder = Path("./data")
day_number = 3
day_text = "day" + str(day_number) + ".txt"
data = data_folder / day_text

# test data
test_data = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

# functions
def queens_case_moves() -> list[np.array]:
    # set up all cases for checking values
    # position values are [row, column] or
    # origin is upper left corner
    UL = np.array([-1, -1])
    UU = np.array([-1, 0])
    UR = np.array([-1, 1])
    LL = np.array([0, -1])
    RR = np.array([0, 1])
    DL = np.array([1, -1])
    DD = np.array([1, 0])
    DR = np.array([1, 1])

    return [UL, UU, UR, LL, RR, DL, DD, DR]

def queens_case(data:list[str], position: np.array, tracking_array:np.array = None):
    for move in queens_case_moves():
        try:
            # apply move
            data_pos = position + move

            # pull coords
            data_pos_row = data_pos[0]
            data_pos_col = data_pos[1]

            # get data at that value
            data_value = data[data_pos_row][data_pos_col]

            if data_value.isnumeric():
                tracking_array[data_pos_row, data_pos_col] = int(data_value)
        except:
            continue

def number_to_the_sides(tracking_array:np.array, data:list[str]=None):
    for rowid in range(tracking_array.shape[0]):
        for colid in range(tracking_array.shape[1]):

            # get array value
            arr_val = tracking_array[rowid, colid]

            # check if value is non-zero
            if arr_val > 0:
                # see if left value is a number and add to tracking array
                try:
                    val_to_left = data[rowid][colid-1]
                    if val_to_left.isnumeric():
                        tracking_array[rowid, colid-1] = val_to_left
                except:
                    continue
                # see if right value is a number and add to tracking array
                try:
                    val_to_right = data[rowid][colid+1]
                    if val_to_right.isnumeric():
                        tracking_array[rowid, colid+1] = val_to_right
                except:
                    continue

# main function
def main():

    with open(data) as f:
    
        # read data
        engine_diagram = f.readlines()
        
        # engine_part_numbers
        engine_part_numbers = []

        # tracking array
        num_rows = len(engine_diagram)
        num_cols = len(engine_diagram[0])

        tracking_array = np.zeros((num_rows, num_cols), dtype=int)

        # perform queens case on symbols
        for rowid, row in enumerate(engine_diagram):
            for columnid, column in enumerate(row):

                # check if value is non-period symbol
                value = engine_diagram[rowid][columnid]

                if value != "." and value.isnumeric() == False:
                    # position
                    position = np.array([rowid, columnid])

                    queens_case(engine_diagram, position, tracking_array)

        # use tracking array to recursively look for numbers left and right of numbers
        for times in range(tracking_array.shape[0] * tracking_array.shape[1]):
            number_to_the_sides(tracking_array, engine_diagram)

        for row in tracking_array:
            # convert np.array to string
            row_str = np.array2string(row)

            # strip out characters
            row_str = row_str.replace("[", "")
            row_str = row_str.replace("]", "")
            row_str = row_str.replace(" ", "")

            # split string at 0's
            split_str = row_str.split("0")

            for string in split_str:
                if string.isnumeric():
                    part_number = int(string)
                    engine_part_numbers.append(part_number)

        sum_of_engine_parts = sum(engine_part_numbers)
        print(f"The sum of the engine part numbers is {sum_of_engine_parts}")

if __name__ == "__main__":
    main()
