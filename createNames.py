# Load pandas
import pandas as pd
import csv

# Initialize variables
names = []
firstName = []
lastName = []
# Populate First Name and Last Name arrays
with open('/Users/ashleypang/Documents/GitHub/Frank Vahid Tools/anonymous_name_tool/firstNames.txt') as f:
    for line in f:
        firstName.append(line.strip())

# Populate First Name and Last Name arrays
with open('/Users/ashleypang/Documents/GitHub/Frank Vahid Tools/anonymous_name_tool/lastNames.txt') as f:
    for line in f:
        lastName.append(line.strip())

for i in firstName:
    for j in lastName:
        names.append(i + ' ' + j)

with open('names_1.txt', 'w') as my_list_file:
    for element in names:
        my_list_file.write('%s\n' % element)