import re

f = open('input.txt', 'r')

count = 0
for s in f:
    line = s.strip()
    m = re.search(r'(..).*\1', line)
    if not m:
        continue
    m = re.search(r'(.).\1', line)
    if not m:
        continue

    count += 1

print(count)

f.close()