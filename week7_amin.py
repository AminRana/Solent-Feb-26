"""
thisset={"jackfruit", "apple", "banana", "orange", "orange"}
print(thisset)
print(len(thisset))
print(type(thisset))
x=set(("1", "2", "3", "4", "5", "6", "7", "8", "9"))
print(x)
print(len(x))
print(type(x))
for y in x:
    print(y)

print("10" in x)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset.add("kiwi")
print(thisset)
del thisset
print(thisset)
"""

#Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["year"])
thisdict["color"]="red"
print(thisdict)
y=thisdict.keys()
print(y)