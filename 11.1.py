import re
name = input('Enter the name of file')
if len(name) < 1:
    fhand = open('regex_sum_197894.txt')
else:
    fhand = open(name)
ttl = 0
for line in fhand:
    line = line.strip()
    lst = re.findall('[0-9]+',line)
    for x in lst:
        x = int(x)
        ttl = ttl+x
print(ttl)
