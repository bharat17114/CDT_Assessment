import csv

correct_ans = ['ans_Q12','10','5','7']
correct_ans2 = ['ans_Q2','2','3','4', '5']


def readcsv():
  temp_list = [] # Initialize  variable temp list
  f = open('values.csv','r') # opens the csv file
  num_lines = sum(1 for line in open('values.csv','r'))
  print("This file has",num_lines,"lines")
  for i in range(0,num_lines): # for every line after that format and append to list
    line = f.readline()
    line = line.rstrip()       #removes trailing characters from line
    questions = line.split(",")
    without_empty_strings = [string for string in questions if string != ""]

    print(without_empty_strings)

  if without_empty_strings == correct_ans:
      print("All entries in Q1 are right")

  else:
      print("One entry in Q1 is wrong")
  # append detials to list #

  if without_empty_strings == correct_ans2:
      print("Q2 right")

  else:
      print("One entry in Q2 is wrong")
    
  temp_list.append(questions)
  f.close() # close the file

    

readcsv()

        
        
