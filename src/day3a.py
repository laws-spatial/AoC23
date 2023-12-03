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

# test = np.zeros((10, 10))
# print(test)
# test[5, 5] = "6"
# print(test)

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

            if arr_val > 0:
                try:
                    val_to_left = data[rowid][colid-1]
                    if val_to_left.is_numeric():
                        tracking_array[rowid, colid-1] = val_to_left
                except:
                    continue
                try:
                    val_to_right = data[rowid][colid+1]
                    if val_to_right.is_numeric():
                        tracking_array[rowid, colid+1] = val_to_right
                except:
                    continue

    return number_to_the_sides()


    
# main function
def main():

    # tracking array
    num_rows = len(test_data)
    num_cols = len(test_data[0])

    tracking_array = np.zeros((num_rows, num_cols))

    # perform queens case on symbols
    for rowid, row in enumerate(test_data):
        for columnid, column in enumerate(row):

            # check if value is non-period symbol
            value = test_data[rowid][columnid]

            if value != "." and value.isnumeric() == False:
                # position
                position = np.array([rowid, columnid])

                queens_case(test_data, position, tracking_array)

    # use tracking array to recursively look for numbers left and right of numbers
    number_to_the_sides(tracking_array)


    # print(tracking_array)
    
if __name__ == "__main__":
    main()
