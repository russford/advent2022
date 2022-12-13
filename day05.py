import re

strings = ["ZN", "MCD", "P"]

strings = ["GTRW",
           "GCHPMSVW",
           "CLTSGM",
           "JHDMWRF",
           "PQLHSWFJ",
           "PJDNFMS",
           "ZBDFGCSJ",
           "RTB",
           "HNWLC"
           ]
moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

with open("day05.txt", "r") as f:
    moves = f.read()

print (strings)

for move in moves.split("\n"):
    n, src, dest = (int(a) for a in re.findall("\d+", move))
    strings[dest-1] = strings[dest-1] + strings[src-1][-n:]
    strings[src-1] = strings[src-1][:-n]

print (''.join(s[-1] for s in strings))