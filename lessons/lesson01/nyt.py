#!/usr/bin/python
# Import required libraries
import sys

# Start a counter and store the textfile in memory
age = 0
total_age = 0
count = 0
clicks = 0
max_age = 0

lines = sys.stdin.readlines()
lines.pop(0)
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
    clean_line = line.strip().split(',')
    age = int(clean_line[0])
    total_age += age
    count = count + int(clean_line[2])
    clicks += int(clean_line[3])
    max_age = max(max_age, age)

average_age = 'Average age: {0:.1f}'.format(float(total_age) / n)
impressions = 'Impression:  {:,}'.format(count)
ctr         = 'CTR:         {0:.2f}%'.format(float(clicks) / count * 100)
max_age_str = 'Max age:     {0:d}'.format(max_age)

content = average_age + '\n' + impressions + '\n' + ctr + '\n' + max_age_str + '\n'
print content
file = open('result.txt', 'w')
file.write(content)
file.close()
