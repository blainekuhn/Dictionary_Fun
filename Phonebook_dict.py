#! /Users/blainekuhn/Git/Python/env/bin/python3

from faker import Faker
from os import path
import os
fake = Faker()


Dict = {"Name": [], "Address": [], "City": [], "State": [], "Zipcode": [], "Phone": []}



def Add_to_dict(count):
  for x in range(count):
    Dict["Name"].insert(len(Dict["Name"]), fake.name())
    Dict["Address"].insert(len(Dict["Address"]), fake.street_address())
    Dict["City"].insert(len(Dict["City"]), fake.city())
    Dict["State"].insert(len(Dict["State"]), fake.state())
    Dict["Zipcode"].insert(len(Dict["Zipcode"]), fake.zipcode())
    Dict["Phone"].insert(len(Dict["Phone"]), fake.phone_number())    
  Write_to_file(Dict)


#  return print(Dict["Name"])
#  return print("%s lives at %s %s, %s. %s." % (Dict["Name"], Dict["Address"], Dict["City"], Dict["State"], Dict["Zipcode"]))
  #for a in range(len(Dict["Name"])):
    #print("%s\t\t%s\t\t%s\t%s\t%s" % (Dict["Name"][a], Dict["Address"][a], Dict["City"][a], Dict["State"][a], Dict["Zipcode"][a]))


def Write_to_file(data):
  for a in range(len(data["Name"])):
    log_file=path.join(os.getcwd(), "Dictionary.log")
    if not path.exists(log_file):
      with open(log_file, 'w') as f:
        f.close()
    with open(path.join(os.getcwd(), "Dictionary.log"), 'a') as f:
      a_data = [data["Name"][a], data["Address"][a], data["City"][a], data["State"][a], data["Zipcode"][a], data["Phone"][a]]
      f.write(str(a_data)+'\n')


Add_to_dict(100)

