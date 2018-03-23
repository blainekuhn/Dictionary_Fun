"""
  This script is to test my ability to create a json file from a dictionary.

  First the script should create a dictionary
  ifthe firs letter is 'B' add another level deep (recurse on all added)
  Then to write this to a file
  Then optional print json content to screen  

  From a question I posted on StackOverflow to create the initial dictionary
  names = [(fake.first_name(), fake.uri()) for i in range(5)]

if dic found in dic[key]
  a.append("[key]"*3)  which ends up being ['[key][key][key]']
  this could be used to ste

"""

import sys, json
from faker import Faker
from random import randint
fake = Faker()
count = [0, 0]

dic_len = 15      ## User changable option
depth = 200      ## User changable option



def build_dic(dic_len, dic, depth):
  if count[0] >= depth:
    return dic
  try:
    if isinstance(dic, (list, tuple)):
      dic = dict(dic)
    if isinstance(dic, dict):
      for counter in range(len(dic)):
        count[0]+=1
        if count[0] < 4444444:
          pass
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


dic = build_dic(dic_len, ([(fake.first_name(), fake.uri()) for i in range(dic_len)]), 1)
walk(dic_len, dic, depth)
print(json.dumps(dic, indent=4))


