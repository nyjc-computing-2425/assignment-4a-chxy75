nric = input('Enter an NRIC number: ')

# Type your code below
nric = nric.lstrip(' ')
a = nric[0]
b = nric[8]
no_raw = list(nric[1:8])
no = []
for number in no_raw:
    no.append(int(number))

table_1 = [2, 7, 6, 5, 4, 3, 2]
table_2 = [
    '0JX', '1ZW', '2IU', '3HT', '4GR', '5FQ', '6EP', '7DN', '8CM', '9BL',
    '10AK'
]
valid = True

if (a == "S" or a == "T" or a == "F" or a == "G") and (len(no) == 7) and (b.isalpha()):

    sum_1 = []
    for i in range(0, len(no)):
        sum_1.append(no[i] * table_1[i])
    sum = int(sum(sum_1))

    if a == 'T' or a == 'G':
        sum = sum + 4

    no, remainder = divmod(sum, 11)
    remainder = int(remainder)
    print(remainder)

    if (a == 'S' or a == 'T') and (b in table_2[remainder][1]):
        valid = True
    elif (a == 'F' or a == 'G') and (b in table_2[remainder][2]):
        valid = True
    else:
        valid = False

else:
    valid = False

if valid:
    print('NRIC is valid.')
else:
    print('NRIC is invalid.')