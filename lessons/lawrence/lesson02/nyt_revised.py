# Import required libraries
import sys

lines = sys.stdin.readlines()
lines.pop(0)

new_header = '"age", "gender,", "signed_in", "avg_click", "agv_impressions", "max_click", "max_impressions"'
sorted_lines = sorted(lines, key = lambda line: (int(line.strip().split(',')[0]), int(line.strip().split(',')[1]), int(line.strip().split(',')[4])))

last_age = None
last_gender = None
last_signed_in = None
new_list = []
inner_list = []

for line in sorted_lines:
    clean_line = line.strip().split(',')
    new_age = int(clean_line[0])
    new_gender = int(clean_line[1])
    new_signed_in = int(clean_line[4])
    new_impressions = int(clean_line[2])
    new_click = int(clean_line[3])

    if last_age != new_age:
        if last_age is not None:
            inner_list[3] /= float(inner_list[7])
            inner_list[4] /= float(inner_list[7])
            new_list.append(inner_list)
        inner_list = [new_age, new_gender, new_signed_in, new_click, new_impressions, new_click, new_impressions, 1]
        last_age = new_age
        last_gender = new_gender
        last_signed_in = new_signed_in
    elif last_gender != new_gender:
        inner_list[3] /= float(inner_list[7])
        inner_list[4] /= float(inner_list[7])
        new_list.append(inner_list)
        inner_list = [new_age, new_gender, new_signed_in, new_click, new_impressions, new_click, new_impressions, 1]
        last_gender = new_gender
    elif last_signed_in != new_signed_in:
        inner_list[3] /= float(inner_list[7])
        inner_list[4] /= float(inner_list[7])
        new_list.append(inner_list)
        inner_list = [new_age, new_gender, new_signed_in, new_click, new_impressions, new_click, new_impressions, 1]
        last_signed_in = new_signed_in
    else:
        inner_list[3] += new_click
        inner_list[4] += new_impressions
        inner_list[5] = max(inner_list[5], new_click)
        inner_list[6] = max(inner_list[6], new_impressions)
        inner_list[7] += 1
new_list.append(inner_list) # Append the last list which is not appended in the loop

file = open('nyt_new.csv', 'w')
file.write(new_header + '\n')
for line in new_list:
    age = '{0:d}'.format(line[0])
    gender = '{0:d}'.format(line[1])
    signed_in = '{0:d}'.format(line[2])
    avg_clicks = '{0:.1f}'.format(line[3])
    avg_impressions = '{0:.1f}'.format(line[4])
    max_clicks = '{0:d}'.format(line[5])
    max_impressions = '{0:d}'.format(line[6])
    file.write(age + ', ' + gender + ', ' + signed_in + ', ' +
        avg_clicks + ', ' + avg_impressions + ', ' + max_clicks + ', ' + max_impressions + '\n')
file.close()
