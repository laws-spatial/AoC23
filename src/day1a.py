# imports
from pathlib import Path

# read data
data_folder = Path("./data")
data = data_folder / "day1a.txt"
print(Path.cwd())
print(data.absolute())


# functions
def num_char(line: str):
    """Return a list of all numeric characters in a string"""
    return [char for char in line if char.isnumeric()]


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

            # get first and last numeric characters
            first_last = first_last_num_chars(num_chars)

            # get sum of all numeric characters
            combined_first_last = combine_num_chars(first_last)

            # append to list
            val_list.append(combined_first_last)

    # sum val_list
    sum_val_list = sum_num_list(val_list)

    # print
    print(sum_val_list)


if __name__ == "__main__":
    main()
