import sys


def quicksort1(a, s):
    p = a[0]
    less = []
    greater = []

    for x in range(s):
        if a[x] < p:
            less.append(a[x])
        elif not a[x] is p:
            greater.append(a[x])

    return less + [p] + greater


def quicksort(a, s):
    if s == 1 or s == 0:
        if s == 0:
            return [None]
        else:
            return [a[0]]

    p = a[0]
    less = []
    greater = []

    for x in range(s):
        if a[x] < p:
            less.append(a[x])
        elif not a[x] is p:
            greater.append(a[x])

    l = quicksort(less, len(less))
    g = quicksort(greater, len(greater))

    if l == [None]:
        tmp = [p] + g
    elif g == [None]:
        tmp = l + [p]
    else:
        tmp = l + [p] + g

    print(" ".join(map(str, tmp)))
    return tmp

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            # a = quicksort1(parsed, size)
            # print(" ".join(map(str, a)))
            quicksort(parsed, size)
