def ex1():
    """Smoll parser that run some multiplication.

       Valid format is `mul(x,y)` where x and y are numbers between 0 and 999.
    """

    tot = 0
    with open('input.txt', 'r') as file:
        for line in file:
            print(f"line: {line}")

    print(f"total is {tot}")


if __name__ == "__main__":
    ex1()
