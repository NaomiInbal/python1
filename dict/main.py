# This is a sample Python script.
def count_chars(my_str):
    my_dict = {}
    for letter in my_str:
        my_dict[letter] = my_str.count(letter)
        if letter == " ":
            del my_dict[letter]
    print(my_dict)


def inverse():
    my_map = {"a": 3, "b": 2, "i": 3}
    new_map = {v: k for (k, v) in my_map.items()}
    print(new_map)


def main():
    # my_str = input("Enter a string ")
    # count_chars(my_str)
    inverse()
    print("uih")


if __name__ == '__main__':
    main()
