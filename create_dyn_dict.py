"""
  This script is to test my ability to create a json file from a dictionary.

  There are several methods defined.
  1.  walk() is the primary way of creating the dictionary
      a. it calls build_dic to do the dictionary creation at each level
      b. it is called with any dictionary
  2.  known_dic_keys() will create a dictionary of specified length using known keys
  3. get_known_dic_info() is called after known_dic_keys() as it uses the very 'known' keys
      a. This will spit out a sorted list of lists with a user entered last name

  
  From a question I posted on StackOverflow to create the initial dictionary
  names = [(fake.first_name(), fake.uri()) for i in range(5)]

if dic found in dic[key]
  a.append("[key]"*3)  which ends up being ['[key][key][key]']
  this could be used to ste

"""

import sys, json
from faker import Faker
from random import randint, choice
fake = Faker()
count = [0, 0]

dic_len = 10      ## User changable option
depth = 300      ## User changable option


def build_dic(dic_len, dic, depth):
  if count[0] >= depth:
    return dic
  elif count[0] == dic_len:
    #print("short one %s " % dic_len)
    walk(dic_len, dic, depth)
  try:
    if isinstance(dic, (list, tuple)):
      print("You didn't send a dictionary")
      return
    if isinstance(dic, dict):
      for counter in range(len(dic)):
        count[0]+=1
        for k,v in dic.items():
          if k[0] == 'B' or k[0] == "M":
            update = [(fake.first_name(), fake.uri()) for i in range(dic_len)]
            update = dict(update)
            dic.update({k: update})
  except RecursionError:
    print("too many iterations")
    print(json.dumps(dic, indent=4))
  return dic


def walk(dic_len, dic, depth):
  if count[0] >= depth:
    return dic  
  for key, item in dic.items():
      if isinstance(item, dict):
        build_dic(dic_len, item, depth)
        walk(dic_len, item, depth)
  check_it(count, dic_len, dic, depth)
  return dic


def check_it(count, dic_len, dic, depth):
  if count[0] < depth and count[0] > dic_len:
    count[1]+=1
    if count[1] == 20:
      sys.exit(print("Try using a larger dic_len and run again.\n"\
            "Unable to reach stated depth with a dic_len of %s." % dic_len))
    print("Rebuilding...\nCurrent dictionary is only %s iterations." % count[0])
    dic = build_dic(dic_len, ([(fake.first_name(), fake.uri()) for i in range(dic_len)]), 1)
    if isinstance(dic, (list, tuple)):
      dic = dict(dic)
      count[0] = 0
      walk(dic_len, dic, depth)

def write_to_file(dic, filename):
  with open(filename, 'w') as f:
    f.write(dic)
    f.close()

def known_dic_keys(dic_len):
  known_dic = {'F_NAME': [], 'L_NAME': [], 'AGE': [], 'P_BIRTH': [], 'SSN': [], 'S_CLEARANCE': []}
  for a in range(dic_len):
    known_dic["F_NAME"].insert(len(known_dic['F_NAME']), fake.first_name())
    known_dic["L_NAME"].insert(len(known_dic['L_NAME']), fake.last_name())
    known_dic["AGE"].insert(len(known_dic['AGE']), randint(1,99))
    known_dic["P_BIRTH"].insert(len(known_dic['P_BIRTH']), list((fake.city(), fake.state())))
    known_dic["SSN"].insert(len(known_dic['SSN']), fake.ssn())
    known_dic["S_CLEARANCE"].insert(len(known_dic['S_CLEARANCE']), choice([True, False]))
  known_dic = dict(known_dic)
    
  return known_dic

def get_known_dic_info(dic):
  result = []
  lst = [0]
  while True:
    check_name = input("Enter a last name to see if it's in the DB. ")
    for a in range(len(dic['L_NAME'])):
      #print(dic['L_NAME'][a])
      if dic['L_NAME'][a] == check_name:
        #print(dic['F_NAME'][a], dic['L_NAME'][a], dic['AGE'][a], dic['P_BIRTH'][a], dic['SSN'][a], dic['S_CLEARANCE'][a])
        lst[0] = True
        item = dic['F_NAME'][a], dic['L_NAME'][a], dic['AGE'][a], dic['P_BIRTH'][a], dic['SSN'][a], dic['S_CLEARANCE'][a]
        item = list(item)
        #print(list(item))
        lst.append(item)
    result = sorted(lst[1:len(lst)])
    for item in result:
      print(item)
    return result



#dic_of_known_keys = known_dic_keys(500)
#dic = build_dic(dic_len+1, ([(fake.first_name(), fake.uri()) for i in range(dic_len)]), 1)
#walk(dic_len, dic, depth)
#print(json.dumps(dic, indent=4))

