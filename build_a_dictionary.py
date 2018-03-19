"""
  build a dcitionary of lists with dictionaries in those lists and possibly more
  using random length words, smaller words become keys and longer words values
  if random word starts with 'n' it's a nested list with a dictionary as the
  only entry[0]

  Noticed a large differnce in run time so I added a timer.
  I was surprised to see the simpler looking code was up to 5 times slower.
  I would think 
"""

from random import Random, randint
import string, random, sys, time
from faker import Faker
fake = Faker()
dic = {}
dics = {}
key = ""

def add_dic(x):
  dic={}
  start = time.time()
  if x > 690:
    print("Please select a value under 690")
    sys.exit()
  for n in range(x):
    while len(dic) < x:
      key = fake.first_name()
      if key in dic.keys():
        break
      val = fake.uri()
      dic[key] = val
  end = time.time()
  runtime = end - start
  #print("It took %s to run add_dic" % runtime)
  return dic


def adds_dic(x):
  start = time.time()
  if x > 690:
    print("Please select a value under 690")
    sys.exit()
  while len(dics) < x:
    dics[fake.first_name()] = [fake.uri()]
  end = time.time()
  runtime = end - start
  print("It took %s to run adds_dic" % runtime)  
  return dics

#print(json.load(add_dic(30)))
#adds_dic(600)
#add_dic(60)

def same_name():
  count=1
  while True:
    b = fake.first_name()
    count+=1
    if 'Jennifer' in b:
      print("this is %s" % b)
      print(count)
      count=1

