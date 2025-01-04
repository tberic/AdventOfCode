from aoc import *

workflows = []
names = []
loc = {}
ratings = []

def unpack(rating):
    x, m, a, s = rating[1:-1].split(',')
    x = int(x[2:])
    m = int(m[2:])
    a = int(a[2:])
    s = int(s[2:])
    return (x, m, a, s)

def satisfies(rating, condition):
    x, m, a, s = unpack(rating)
    return eval(condition)

def go(rating, name):
    workflow = workflows[loc[name]]
    
    rules = workflow.split(',')

    for rule in rules:
        if rule == 'R' or rule == 'A':
            return rule
        if ':' not in rule:
            return go(rating, rule)
        
        cond, outcome = rule.split(':')
        if satisfies(rating, cond):
            if outcome == 'A' or outcome == 'R':
                return outcome
            return go(rating, outcome)                
    

f = open('input.txt', 'r')

# input
workflowsDone = False
for line in f:
    if line.strip() == "":
        if not workflowsDone:
            workflowsDone = True
            continue
    
    if not workflowsDone:        
        name, workflow = line.strip().split('{')
        workflows.append(workflow[:-1])
        names.append(name)
        loc[name] = len(names) - 1
    else:
        ratings.append(line.strip())

sum = 0
x = m = a = s = 0
for rating in ratings:
    res = go(rating, 'in')
    if res == 'A':
        x, m, a, s = unpack(rating)
        sum += x+m+a+s
print(sum)