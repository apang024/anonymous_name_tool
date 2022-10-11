# 10 number userID ex:14256 44578
# 00012 81619

#  function?
# h(k) = k mod n
# Here, h(k) is the  value obtained by dividing the key value k by size of  table n using the remainder. It is best that n is a prime number as that makes sure the keys are distributed with more uniformity.
# An example of the Division Method is as follows −

# k=1276
# n=10
# h(1276) = 1276 mod 10
# = 6

# Load pandas
import pandas as pd
import csv

# Initialize variables
names = []
firstName = []
lastName = []
netID = []
output = []

# Populate First Name and Last Name arrays
with open('/Users/ashleypang/Documents/GitHub/Frank Vahid Tools/anonymous_name_tool/txtFiles/names_1.txt') as f:
    for line in f:
        names.append(line)
        firstName.append(line.split()[0])
        lastName.append(line.split()[1])

# Read csv file
filename = input('Enter logfile name: ')
df = pd.read_csv('/Users/ashleypang/Documents/GitHub/Frank Vahid Tools/anonymous_name_tool/logFiles/' + filename)
df = df[df.role == 'Student']

# Update column names if necessary
# Enables support for log files from learn.zybooks.com and Mode
df.columns = df.columns.str.replace('\(US/Pacific\)', '', regex=True)
df.columns = df.columns.str.replace('is_submission', 'submission')
df.columns = df.columns.str.replace('content_resource_id', 'lab_id')

# Extract userIDs
for i, row in enumerate(df.itertuples()):
    # Update original log file
    df.iat[i,5] = firstName[row.user_id]
    df.iat[i,6] = lastName[row.user_id]
    # Keep an array of ids and names
    output.append(str(row.user_id) + ' ' + firstName[row.user_id] + ' ' + lastName[row.user_id])

df.to_csv('/Users/ashleypang/Documents/GitHub/Frank Vahid Tools/anonymous_name_tool/outputLogFiles/copy_of_' + filename, index=False)

# with open("output.csv", "w") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['name'])
#     writer.writerows(output)