"""Tests can be ran with `python3 -m doctest ex2.py`"""

def ex2():
    """
    TLDR: for each elem in right, tot = right * (occurence in left)
    Can be simplified by for unique e in right, tot = e * (nb e in left) * (nb e in right)

    Examples:
    >>> ex2()
    total occurence is 24643097
    """
    left, right = [], []

    with open('input.txt', 'r') as file:
        for line in file:
            l, r = line.split('   ')
            # print(f"left: {l}, right: {r}")

            left.append(int(l))
            right.append(int(r))

    done = {}

    tot = 0
    for l in left:
        if l in done:
            continue

        done[l] = True
        tot += l*(right.count(l)*left.count(l))

    # 24643097 expected
    print(f"total occurence is {tot}")


if __name__ == "__main__":
    ex2()
