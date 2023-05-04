# Author: fransay
# Date: 01/05/2023
# Description: Project Euler (Sum of even fibonacci numbers)

import time as t


def even(number) -> bool:
    """
    returns a boolean representation of the even status
    :param number:
    :return:
    """
    is_even = number % 2 == 0
    return is_even


def main():
    start_time = t.time()  # init stop clock
    LIMIT = 4000000
    SUM = 0
    count_number = 0
    start_count_number, next_count_number = count_number, count_number + 1
    while start_count_number <= LIMIT:
        third_number = start_count_number + next_count_number
        if even(third_number):
            SUM = SUM + third_number
        start_count_number, next_count_number = next_count_number, third_number
        count_number += 1
        # print(third_number, end=" \n")
    print("SUM: ", SUM)
    end_time = t.time()  # end stop clock counter in seconds
    time_elapsed = end_time - start_time
    print(f'Runtime: {time_elapsed} seconds')


if __name__ == '__main__':
    main()
