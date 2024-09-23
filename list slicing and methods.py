marks = [85, 94, 76, 63, 48]
print (marks[1:4])

#list methods
list= [2, 1, 3]

list.append(4) #adds one element at the end 
print(list)

list.sort() #sorts in ascending order
print(list.sort())
print(list)

print(list.sort(reverse=True))  #sorts in descending order
print(list)

list.reverse()  #reverses list
print(list)

list.remove(1) #removes first occurrence of element
print(list)

list.pop(2) #removes element at idx
print(list)