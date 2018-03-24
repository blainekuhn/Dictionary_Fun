import string
a = {
  "A" : ["Abacus", "aardvark", "Ant"],
  "B" : ["Boatload", "Badlands", "broken"],
  "c" : "Coriander",
  "D" : "Dork",
  "E" : "Ecplipse",
  3 : ["a", "B", "c"],
  4 : ["D", "e", "F"],
  "%" : ["Percentage"]
  }

alphabet = string.ascii_uppercase
letters = {}
numbers = {}

let = string.ascii_letters

def letters_numbers(a):
  for x in a.keys():
    if str(x) in let:
      letters[x.upper()] = a[x]
    else:
      numbers[x] = a[x]
      pass
  print("The letters dict is %s\nThe numbers dict is %s." % (letters, numbers))
  get_items(letters)


def get_items(a):
  for x in a.keys():
    pass

#call above as an argument to get the contents of each in letters_numbers()

letters_numbers(a)

#insert Name c["Name"].insert(0,"Jill")
#insert Address c["Address"].insert(0,"This is Jill's address")
