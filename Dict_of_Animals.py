#! /usr/bin/env python
import string


Dict = {"Animal": [], "Color": [], "Legs": [], "Fur": [], "Scales": []}
Alphabet = string.ascii_uppercase

how_many = int(input("How many animals will you enter today? "))

for entry in range(0,how_many):
  animal = input("Enter one type of animal. ")
  color = input("What color is your %s? " % animal)
  legs = input("How many legs does your %s %s have? " % (color, animal))
  fur = input("My %s has fur. True or False? " % animal).lower()

  if fur == 'true':
    scales = "false"
  if fur == "true" or fur == "false":
    pass
  else:
    while True:
      fur = input("Please enter True of False.  My %s has fur. " % animal).lower()
      if fur == "true":
        scales = "false"
      if fur == "true" or fur == "false":
        break

  if fur == "false":
    scales = input("My %s has scales. True or False? " % animal).lower()
  if scales == "true" or scales == "false":
    pass
  else:
    while True:
      scales = input("Please enter True of False.  My %s has scales. " % animal).lower()
      if scales == "true" or scales == "false":
        break

  Dict["Animal"].insert(len(Dict["Animal"]), animal)
  Dict["Color"].insert(len(Dict["Animal"]), color)
  Dict["Legs"].insert(len(Dict["Animal"]), legs)
  Dict["Fur"].insert(len(Dict["Animal"]), fur)
  Dict["Scales"].insert(len(Dict["Animal"]), scales)


more_info = input("Here's a list of animals. Which do you want to know more about, %s? " % Dict["Animal"])


for a in range(len(Dict["Animal"])):
  if more_info == Dict["Animal"][a]:
    if Dict["Fur"][a] == "true":
      print("Your %s is %s, has %s legs, and fur." % ( Dict["Animal"][a], Dict["Color"][a], Dict["Legs"][a]))
    elif Dict["Scales"][a] == "true":
      print("Your %s is %s, has %s legs, and scales." % ( Dict["Animal"][a], Dict["Color"][a], Dict["Legs"][a]))
  

