def dfs(x, removed, dist):
    s = [x]
    while s:
        u = s.pop()
        for v in g[u]:
            if v[0] in removed:
                continue
            dist[v[0]] = dist[u] + v[1]
            if dist[v[0]] - dist[x] > a[v[0]]:
                removed.add(v[0])
            else:
                s.append(v[0])


n = int(input())
a = [0] + list(map(int, input().split()))
g = [list() for _ in range(n+1)]
for u in range(2, n+1):
    v, c = map(int, input().split())
    g[v].append((u, c))
dist = [0 for _ in range(n+1)]
removed = set()
stack = [1]
r = 0

while stack:
    u = stack.pop()
    dfs(u, removed, dist)
    r += 1
    for v in g[u]:
        if v[0] in removed:
            continue
        stack.append(v[0])

print(n - r)
