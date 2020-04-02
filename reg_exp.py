import re
file = open('data1.txt')
sum = 0
for line in file:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    for num in nums:
        sum += int(num)
print(sum)
