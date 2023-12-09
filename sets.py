# set - collection of unique characters.
# no element can appear twice in a 'set'

# create an empty set
mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
mySet.add(3)


mySet.remove(2)
print(mySet)

print(f'My Set has {len(mySet)} elements')
