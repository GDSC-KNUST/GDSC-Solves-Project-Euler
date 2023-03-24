# author @blackprince001

def natural_mod_3_5(n: int) -> list[int]:
    nums = []
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    return nums

def sum_elements(arr: list[int]) -> int:
    return sum(arr)


if __name__ == "__main__":
    to_1000 = natural_mod_3_5(1000)
    sum_to_1000 = sum_elements(to_1000)

    print(f"Sum of multiples of 3 and 5 from 1 to 1000 is {sum_to_1000}")