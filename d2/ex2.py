from typing import List

def test_line(elems: List[int]) -> bool:
    """Implement the line check - aka:
       - elem must be sorted (whatever the order)
       - each elem must be at most 3 a part from it's neighbor
    """
    minToMax = False
    match elems:
        case elems if sorted(elems) == elems:
            minToMax = True
            print(f" --< {len(elems)} elems are sorted from min to max {elems}")
        case elems if  sorted(elems, reverse=True) == elems:
            minToMax = False
            print(f" --> {len(elems)} elems are sorted from max to min {elems}")
        case _:
            print(f"[STOP] elems are not sorted {elems}")
            return False

    for i in range(len(elems)):
        match i:
            case 0:
                # Skip first elem check;.
                continue
            case i if elems[i] == elems[i - 1]:
                print(f"[STOP] elem {i} and n-1 are equal")
                return False
            case i if minToMax and elems[i]-elems[i-1] > 3:
                print(f"[STOP] entry {i} is more than +3 from n-1  ({elems[i]} - {elems[i-1]} > 3)")
                return False
            case i if not minToMax and elems[i-1]-elems[i] > 3:
                print(f"[STOP] entry {i} is less than -3 from n-1  ({elems[i-1]} - {elems[i]} > 3)")
                return False

    print(f"[OK] +1")
    return True

def mutate_and_retry(entries: List[int]) -> bool:
    """Mutate the list by remove 1 elem, and test each use case"""
    for i in range(len(entries)):
        copy = entries.copy()
        del copy[i]
        print(f"[RETRY] mutation [{i}] {copy}")
        if test_line(copy):
            print(f"[RETRY--OK] mutation {i} is valid")
            return True

    return False

def ex2():
    """
    See https://adventofcode.com/2024/day/2.

    TLDR: for each entry
    -> all elem must are sorted (min to max or max to min)
    -> each elem must be 1 <= 3 lower or greater than it's neighbors.
    -> each list has a 1 elem error limit, so retry each case (monkey-brute-force, yup, sorry mum :see_no_evil:


    Examples:
    >>> ex1()
    total correct entries: 436
    """
    tot = 0

    with open('input.txt', 'r') as file:
        for line in file:

            if line == "\n":
                continue

            str_elems = line.strip().split(" ")
            elems = [int(e) for e in str_elems]

            if test_line(elems) or mutate_and_retry(elems):
                tot += 1

    print(f"total correct entries: {tot}")


if __name__ == "__main__":
    ex2()
