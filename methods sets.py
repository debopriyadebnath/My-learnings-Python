#set.add (adds an element)
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege")
collection.add((1,2,3))
#collection.add([1,2,3]) #cant pass list

print(collection)

#set.clear() (empties the set)
collection.clear()
print(collection)

#set.pop() removes any random value
collection = {"hello", "apnacollege", "world", "coding","python"}
print(collection.pop())

#set.union (combines both set values and return new)
set1= {1,2,3}
set2= {2,3,4}
print(set1.union(set2))

#set.intersection (combines common values and return new)
set1= {1,2,3}
set2= {2,3,4}
print(set1.intersection(set2))