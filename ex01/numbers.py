def read_numbers():
    with open("numbers.txt", "r") as f:
        txt = f.read()
    numbers_lst = txt[:-1].split(",")
    for number in numbers_lst:
        print(number)


if __name__ == "__main__":
    read_numbers()
