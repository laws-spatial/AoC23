# imports
from pathlib import Path

# read data
data_folder = Path("./data")
day_number = 2
day_text = "day" + str(day_number) + ".txt"
data = data_folder / day_text

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

    # set thresholds
    thresholds = dict(red=12, green=13, blue=14)

    # add up ids
    id_count = 0

    # iteration
    with open(data) as f:
        for line in f:
            # :
            split_colon = split_at_colon(line)
            game_id_string = split_colon[0]
            after_colon = split_colon[1]

            # ;
            split_semicolon = split_at_semicolon(after_colon)

            # ,
            split_comma = split_at_comma(split_semicolon)

            # possible?
            possible = True

            # count, color
            for drawn_cubes in split_comma:
                count, color = split_count_and_color(drawn_cubes)

                if count > thresholds[color]:
                    possible = False

            if possible == True:
                game_id = split_game_and_id(game_id_string)
                id_count += game_id
    
    print(f"The final count of all possible game ID's is {id_count}")
                

if __name__ == "__main__":
    main()
