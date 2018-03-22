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
fake = Faker()

def build_dic(dic_len, dic):
  if isinstance(dic, (list, tuple)):
    dic = dict(dic)
  if isinstance(dic, dict):
    for counter in range(len(dic)):
      for k,v in dic.items():
        if k[0] == 'B' or k[0] == "M":
          update = [(fake.first_name(), fake.uri()) for i in range(5)]
          update = dict(update)
          dic.update({k: update})
  return dic

def walk(dic):
  for key, item in dic.items():
      #print(type(item))
      if isinstance(item, dict):
        build_dic(5, item)
        walk(item)
  return dic

a = build_dic(10, ([(fake.first_name(), fake.uri()) for i in range(10)]))
walk(a)
print(json.dumps(a, indent=4))
