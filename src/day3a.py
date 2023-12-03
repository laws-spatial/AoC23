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

def queens_case(data:list[str], position: np.array):
    for move in queens_case_moves():
        try:
            # apply move
            data_pos = position + move

            # pull coords
            data_pos_row = data_pos[0]
            data_pos_col = data_pos[1]

            # get data at that value
            data_value = data[data_pos_row][data_pos_col]
        
            print(f"Data value {data_value} at position {data_pos} with move {move}")
        except:
            continue

# main function
def main():
    for rowid, row in enumerate(test_data):
        for columnid, column in enumerate(row):


            # check if value is non-period symbol
            value = test_data[rowid][columnid]

            if value != "." and value.isnumeric() == False:
                # position
                position = np.array([rowid, columnid])

                queens_case(test_data, position)
    
if __name__ == "__main__":
    main()
