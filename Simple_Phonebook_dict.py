#! /Users/blainekuhn/Scripts/env/bin/python3

Dict = {"Name": [], "Address": [], "City": [], "State": [], "Zipcode": []}

def Add_to_dict():
  name = input("Enter the persons name: ")
  address = input("...and thier street address? ")
  city = input("What city do they live? ")
  state = input("...and that's in what state? ")
  zipcode = input("What's the zipcode? ")
  Dict["Name"].insert(len(Dict["Name"]), name)
  Dict["Address"].insert(len(Dict["Address"]), address)
  Dict["City"].insert(len(Dict["City"]), city)
  Dict["State"].insert(len(Dict["State"]), state)
  Dict["Zipcode"].insert(len(Dict["Zipcode"]), zipcode)
  return print("%s lives at %s %s, %s. %s." % (Dict["Name"], Dict["Address"], Dict["City"], Dict["State"], Dict["Zipcode"]))


Add_to_dict()

