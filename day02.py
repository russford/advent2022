

coding = {"X":"A", "Y":"B", "Z":"C"}
with open ("day02.txt", "r") as f:
    plan = [l[0]+coding[l[2]] for l in f.read().split("\n")]

# plan = ["AB", "BA", "CC"]

def part1 (data, coding):
    scores = {"AA": 1+3, "AB": 2+6, "AC":3+0,
              "BA": 1+0, "BB": 2+3, "BC":3+6,
              "CA": 1+6, "CB": 2+0, "CC":3+3
              }

    score = sum([scores[g] for g in data])
    return score

def part2 (data, coding):
    

print (part1(plan, coding))

print (part2(plan, coding))

