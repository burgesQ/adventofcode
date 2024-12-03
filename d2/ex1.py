def ex1():
    """
    See https://adventofcode.com/2024/day/2.

    TLDR: for each elem
    -> all elem are sorted (min to max or max to min)
    -> each elem must be 1 <= 3 lower or greater than it's neighbors.


    Examples:
    >>> ex1()
    total correct entries: 383
    """
    tot = 0

    with open('input.txt', 'r') as file:
        for line in file:

            if line == "\n":
                continue

            str_elems = line.strip().split(" ")
            elems = [int(e) for e in str_elems]
            tot_elems = len(elems)

            # print(f"{tot_elems} elements in list  {elems}")

            # By default, we assume False
            minToMax = False

            if sorted(elems) == elems:
                minToMax = True
                # print(f"{tot_elems} elems are sorted from min to max {elems}")
            elif sorted(elems, reverse=True) == elems:
                minToMax = False
                # print(f"{tot_elems} elems are sorted from max to min {elems}")
            else:
                # print(f"[STOP] elems are not sorted {elems}")
                continue


            valid = True
            for i in range(tot_elems):
                # Skip first elem check;.
                if i == 0:
                    continue

                # Stop if elem n and n-1 are equal.
                elif elems[i] == elems[i - 1]:
                    # print(f"[STOP] elem {i} and n-1 are equal")
                    valid = False
                    break

                # Stop if minToMax and n is more than +3 than n-1.
                elif minToMax and elems[i]-elems[i-1] > 3:
                    # print(f"[STOP] entry {i} is more than +3 from n-1  ({elems[i]} - {elems[i-1]} > 3)")
                    valid = False
                    break

                # Stop if maxToMin and n is more than -3 than n-1.
                elif not minToMax and elems[i-1]-elems[i] > 3:
                    # print(f"[STOP] entry {i} is less than -3 from n-1  ({elems[i-1]} - {elems[i]} > 3)")
                    valid = False
                    break


            # List is ok
            if valid:
                # print("[OK] +1")
                tot += 1



    print(f"total correct entries: {tot}")


if __name__ == "__main__":
    ex1()
