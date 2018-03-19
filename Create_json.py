"""
  This script is to test my ability to create a json file from a dictionary.

  First the script should create a dictionary
  Then to write this to a file
  Then optional print json content to screen  
"""

import sys, json
from build_a_dictionary import add_dic
from pprint import pprint

dic = add_dic(10)
dic1 = {}
dic2 = {}
dic3 = {}

def build_dic(dic_len):
  dic = add_dic(10)
  dic1 = add_dic(dic_len)
#  dic2 = {}
#  dic3 = {}
  for key in dic1.keys():
    print(key, "\t", dic1[key])
    dic2[key] = add_dic(8)
  #if key in dic.keys():
   # for key2 in dic2.keys():
#      dic2[key][key2] = add_dic(4)


#  for key in dic2.keys():
#    dic3[key] = add_dic(4)
#    for a in dic2[key1]:
#      if dic2[key1][key1][0] == 'B':
#        dic2[key1] = add_dic(4)

        #for b in key2:
            #if b == 'D':
              #print("madde it here")
              #dic3[key2] = dic2[key2] = dic2.values()



build_dic(10)
print(json.dumps(dic2, indent=4))
