def main():
    print("Hello from practice!")


def two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print([num_map[complement], i])
        num_map[num] = i


if __name__ == "__main__":
    main()
    two_sum()
