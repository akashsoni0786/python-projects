l = []
s = []
for _ in range(int(input())):
    name = input()
    l.append(name)
    score = float(input())
    l.append(score)
    s.append(score)

a = len(s)
print(s[1])
j=min(s)
print(j)
for i in range(0, a):
    if j == a[i]:
        print(a[i - 1])



