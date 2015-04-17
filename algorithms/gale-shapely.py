import queue

# x => men : preferences
# y => women: preferences


def match(x, y):
    free_x = set(x)
    res = {}
    print(123)
    while free_x:
        print(123)
        m = free_x.pop()
        w = x[m].get()
        print((m, w))
        if w in res:
            res.add((m, w))
        else:
            if y[w].index(res[y]) > y[y].index(m):
                d = res.pop(y, None)
                free_x.add(d)
                res[w] = m
            else:
                free_x.add(m)

    print("\n".join(map(str, [(i, res[i]) for i in res])))

if __name__ == "__main__":
    Queue = queue.Queue
    a = {"A": Queue("YXZ"), "B": Queue("ZYX"), "C": Queue("XZY")}
    b = {"X": list("BAC"), "Y": list("CBA"), "Z": list("ACB")}
    match(a, b)