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
	age = int(line.strip().split(',')[0])
	total_age += age
	count = count + int(line.strip().split(',')[2])
	clicks += int(line.strip().split(',')[3])
	max_age = max(max_age, age)

print 'Average age: {0:.1f}'.format(float(total_age) / n)
print 'Impression:  {:,}'.format(count)
print 'CTR:         {0:.2f}%'.format(float(clicks) / count * 100)
print 'Max age:    ', max_age
