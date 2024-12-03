"""Tests can be ran with `python3 -m doctest ex1.py`"""

def ex1():
    """
    Calculate distance betwewen elem from input list.
    See https://adventofcode.com/2024/day/1 for more info

    Examples:
    >>> ex1()
    total distance is 2769675
    """
    left, right = [], []

    with open('input.txt', 'r') as file:
        for line in file:
            l, r = line.split('   ')
            # print(f"left: {l}, right: {r}")

            left.append(int(l))
            right.append(int(r))

    left.sort()
    right.sort()

    tot = 0
    for l, r in zip(left, right):
        if l > r:
            # print(f"adding  l ({l}) - r ({r}) = {l-r}")
            tot += (l - r)
        elif r > l:
            # print(f"adding  r ({r}) - l ({l}) = {r-l}")
            tot += (r - l)
    print(f"total distance is {tot}")


if __name__ == "__main__":
    ex1()
