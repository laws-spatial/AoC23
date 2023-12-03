# imports
from pathlib import Path
import numpy as np

# read data
data_folder = Path("./data")
day_number = 2
day_text = "day" + str(day_number) + ".txt"
data = data_folder / day_text

# test data
test_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

# functions
def flatten_list(list_lists: list[list]):
    return [item.strip() for row in list_lists for item in row]

def split_at_colon(string:str):
    # break string into sections before and after colon :
    return string.split(":")

def split_at_semicolon(string:str):
    # break string into sections before and after semicolon ;
    return string.split(";")

def split_at_comma(list: list[str]):
    # break each string in list into sections based on comma and strips whitespace
    split_list = [string.split(",") for string in list]
    return flatten_list(split_list)

def split_count_and_color(string: str):
    # split string into a count and coor
    count, color = string.split(" ")

    # convert count to integer
    count = int(count)

    return count, color

def split_game_and_id(string:str):
    # split into game and id number
    game, id = string.split(" ")
    
    # convert id to integer
    id = int(id)

    return id

# main function
def main():

    # add up ids
    power_count = 0

    # iteration
    with open(data) as f:
        for line in f:

            # get counts for all
            counts = dict(red = [],
            blue = [],
            green = [])

            # minimum number
            max_drawn_cubes = []

            # :
            split_colon = split_at_colon(line)
            drawn_cubes = split_colon[1]

            # ;
            split_semicolon = split_at_semicolon(drawn_cubes)

            # ,
            split_comma = split_at_comma(split_semicolon)

            # create full lists of pulled out numbers of cubes
            for drawn_cubes in split_comma:
                count, color = split_count_and_color(drawn_cubes)

                counts[color].append(count)

            print(counts)
            # find max values from each lit and add to min drawn cubes
            for values in counts.values():
                try:
                    max_value = max(values)
                    max_drawn_cubes.append(max_value)
                except:
                    continue

            # calculate power
            row_power = np.prod(max_drawn_cubes)

            # add to power_count
            power_count += row_power



    
    print(f"The final value of all the powers is {power_count}")
                

if __name__ == "__main__":
    main()
