from aoc import *

workflows = []
names = []
loc = {}

def adjustLess(cond, num):
    condNew = cond.copy()
    for i in range(num-1, 4000):
        condNew[i] = 0
    return condNew

def adjustGreater(cond, num):
    condNew = cond.copy()
    for i in range(num):
        condNew[i] = 0
    return condNew

def parse(s):
    conds = [cond for cond in s.split(' ') if cond != '']
    x = [1 for i in range(4000)]
    m = [1 for i in range(4000)]
    a = [1 for i in range(4000)]
    s = [1 for i in range(4000)]
    for cond in conds:
        if '<' in cond:
            var, num = cond.split('<')
            num = int(num)
            if var == 'x':
                x = adjustLess(x, num)
            elif var == 'm':
                m = adjustLess(m, num)
            elif var == 'a':
                a = adjustLess(a, num)
            elif var == 's':
                s = adjustLess(s, num)
        elif '>' in cond:
            var, num = cond.split('>')
            num = int(num)
            if var == 'x':
                x = adjustGreater(x, num)
            elif var == 'm':
                m = adjustGreater(m, num)
            elif var == 'a':
                a = adjustGreater(a, num)
            elif var == 's':
                s = adjustGreater(s, num)
        else:
            print('ERROR: parse')

    return sum(x) * sum(m) * sum(a) * sum(s)

def negate(s):
    if '<' in s:
        var, num = s.split('<')
        return var + '>' + str(int(num)-1)
    if '>' in s:
        var, num = s.split('>')
        return var + '<' + str(int(num)+1)
    print('ERROR: negate')

def make_tree(node, conditions):
    if node == 'R':
        return 0
    
    if node == 'A':
        return parse(conditions)
    
    workflow = workflows[loc[node]]
    rules = workflow.split(',')
    count = 0
    newRule = ''
    for rule in rules:
        if ':' not in rule:
            count += make_tree(rule, conditions + ' ' + newRule)
        else:
            cond, dest = rule.split(':')
            count += make_tree(dest, conditions + ' ' + newRule + ' ' + cond)
            newRule = newRule + ' ' + negate(cond)

    return count

f = open('input.txt', 'r')

workflowsDone = False
for line in f:
    if line.strip() == "":
        break
    
    name, workflow = line.strip().split('{')
    workflows.append(workflow[:-1])
    names.append(name)
    loc[name] = len(names) - 1

print( make_tree('in', "") )