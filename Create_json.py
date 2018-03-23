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
count = [0]
def build_dic(dic_len, dic):
  try:
    if isinstance(dic, (list, tuple)):
      dic = dict(dic)
    if isinstance(dic, dict):
      for counter in range(len(dic)):
        for k,v in dic.items():
          if k[0] == 'B' or k[0] == "M":
            update = [(fake.first_name(), fake.uri()) for i in range(dic_len)]
            update = dict(update)
            dic.update({k: update})
#        count[0]+=1
  except RecursionError:
    print("too many iterations")
    print(json.dumps(dic, indent=4))
#  if count[0] > 100*(10-1):
#    print(count)
  return dic

def walk(dic_len, dic):
  #count[0]+=1
  if count[0] > 10:
    sys.exit(print(json.dumps(dic, indent=4)))
  for key, item in dic.items():
      #print(type(item))
      if isinstance(item, dict):
        build_dic(dic_len, item)
        walk(dic_len, item)
        print(count)
        count[0]+=1
  return dic


dic = build_dic(10, ([(fake.first_name(), fake.uri()) for i in range(10)]))
walk(len(dic), dic)
print(json.dumps(dic, indent=4))

"""
good seeds to use:
  5, 8, 300
  11, 8, 460 s/m
  10, 8, 460 m
  `6, 8, 460 m
  
"""
