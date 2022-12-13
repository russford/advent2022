import collections

def part1 (string):
    hash = collections.defaultdict(int)
    for s in string[:4]:
        hash[s] += 1
    for i, c in enumerate(string[4:]):
        if all(v<=1 for v in hash.values()):
            break
        hash[string[i]] -= 1
        hash[string[i+4]] += 1
    return i+4

def part2 (string):
    hash = collections.defaultdict(int)
    for s in string[:14]:
        hash[s] += 1
    for i, c in enumerate(string[14:]):
        if all(v<=1 for v in hash.values()):
            break
        hash[string[i]] -= 1
        hash[string[i+14]] += 1
    return i+14


print(part2("bvwbjplbgvbhsrlpgdmjqwftvncz"))
print(part2("nppdvjthqldpwncqszvftbrmjlhg"))
print(part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print(part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

print(part2(open("day06.txt", "r").read()))