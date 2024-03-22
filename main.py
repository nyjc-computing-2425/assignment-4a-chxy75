nric = input('Enter an NRIC number: ')


# Type your code below
v = True
valid = True

if len(nric) == 9:
  v = True
else:
  v = False

if v is True:
  nric = nric.lstrip(' ')
  a = nric[0]
  b = nric[8]
  no = list(nric[1:8])

  table_1 = [2, 7, 6, 5, 4, 3, 2]
  table_2 = [
    '0JX', '1ZW', '2IU', '3HT', '4GR', '5FQ', '6EP', '7DN', '8CM', '9BL',
    '10AK'
  ]


  if (a == "S" or a == "T" or a == "F" or a == "G") and (len(no) == 7) and (b.isalpha()):

      sum_1 = []
      for i in range(0, len(no)):
          sum_1.append(int(no[i]) * table_1[i])
      sum = int(sum(sum_1))

      if a == 'T' or a == 'G':
        sum = sum + 4
      else: 
        sum = sum + 0

      no, remainder = divmod(sum, 11)
    #print(no,remainder)
      remainder = int(remainder)
    #print(remainder)
    #print(table_2[remainder][2])
  

      if (a == 'S' or a == 'T') and (b in table_2[remainder][-2]):
          valid = True
        #print('1')
      elif (a == 'F' or a == 'G') and (b in table_2[remainder][-1]):
          valid = True
        #print('2')
      else:
          valid = False
        #print('3')

  else:
      valid = False
    #print('4')

  if valid:
      print('NRIC is valid.')
  else:
      print('NRIC is invalid.')
else:
  print('NRIC is invalid.')