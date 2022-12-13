

with open ("day01.txt") as f:
    data = [[int(k) for k in l.split("\n")] for l in f.read().split("\n\n")]

print (max((sum(d) for d in data)))

cals = sorted([sum(d) for d in data])

print (sum(cals[-3:]))