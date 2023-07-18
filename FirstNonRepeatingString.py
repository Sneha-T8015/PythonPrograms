A="aabbc"
l = []
m = {}
ans = ''
for x in A:
    if x not in m:
        l.append(x)
        m[x]=1
    else:
        if x in l:
            l.remove(x)
    ans += l[0] if l else '#'
print(ans)
