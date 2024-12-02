"""Test can be ran with `python3 -m doctest ex2.py`"""

def ex2():
    """
    TLDR: for each elem in right, tot = right * (occurence in left)

    Examples:
    >>> ex1()
    total occurence is 24643097
    """
    left, right = [], []

    with open('input.txt', 'r') as file:
        for line in file:
            l, r = line.split('   ')
            # print(f"left: {l}, right: {r}")

            left.append(int(l))
            right.append(int(r))

    print(f" {len(left)} elem in left and right")

    done = {}

    tot = 0
    for l in left:
        l = int(l)

        if l in done:
            continue

        done[l] = True
        tot += l*(right.count(l)*left.count(l))

    # 24643097 expected
    print(f"total occurence is {tot}")

if __name__ == "__main__":
    ex2()
