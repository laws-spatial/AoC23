# imports
from pathlib import Path

# read data
data_folder = Path("./data")
data = data_folder / "day1.txt"
print(Path.cwd())
print(data.absolute())

# constants
# nums_spelled_out = {
#     "one": "1",
#     "two": "2",
#     "three": "3",
#     "four": "4",
#     "five": "5",
#     "six": "6",
#     "seven": "7",
#     "eight": "8",
#     "nine": "9",
# }
nums_spelled_out = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

# functions
def num_char(line: str):
    """Return a list of all numeric characters in a string"""
    num_chars_dict = {}

    # check if any of the spelled out numbers are in the line
    for key, value in nums_spelled_out.items():
        # if line.find(key) != -1:
        #     num_chars_dict[line.find(key)] = value
        line = line.replace(key, value)

    # check if any of the numbers are in the line
    for idx, char in enumerate(line):
        if char.isnumeric():
            num_chars_dict[idx] = char

    # sort the dictionary by key
    sorted_num_dict = dict(sorted(num_chars_dict.items()))

    # return the values
    num_chars_list = [value for value in sorted_num_dict.values()]

    return num_chars_list


def first_last_num_chars(list: list[str]):
    """Return a list of the first and last numeric characters in a list"""
    return [list[0], list[-1]]


def combine_num_chars(list: list[str]):
    """Combine numeric characters in a list into a single number"""
    return int("".join(list))


def sum_num_list(list: list[int]):
    """Return the sum of all numeric characters in a list"""
    return sum([val for val in list])


def main():
    # values
    val_list = []

    with open(data, "r") as f:
        for line in f:
            # get all numeric characters
            num_chars = num_char(line)
            print(num_chars)
            # get first and last numeric characters
            first_last = first_last_num_chars(num_chars)
            print(first_last)
            # get sum of all numeric characters
            combined_first_last = combine_num_chars(first_last)

            # append to list
            val_list.append(combined_first_last)

    # sum val_list
    sum_val_list = sum_num_list(val_list)

    # print
    print(f"The sum of all of the values is {sum_val_list}")


if __name__ == "__main__":
    main()
