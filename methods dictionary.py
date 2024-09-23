info ={  
    "key" : "value",
    "name" : "debopriya debnath",
    "learning" : "coding",
    "age": 20
    

}
print(type(info)) 

print(info["key"])


#empty dic
null_dict = {}
print(null_dict)

#nested dic
student = {
     "name" : "rahul kumar",
     "subjects": {
         "phy" : 97,
         "chem" : 98,
         "math" : 95

     }
}





#myDict.keys() returns all keys 
print(list(student.keys()))


#myDict.values() returns all values
print(list(student.values()))


#myDict.items() returns all (key, val) pairs as tuple
pairs= list(student.items())
print(pairs[0])

#myDict.get("key") returns the key accordng to value
print(student.get("name"))

##print(student["name2"]) #error
##print(student.get("name2")) #no error -- none


#myDict.update(newDict)  inserts the specified items to tge dictionary
student.update({"city" : "delhi"})
print(student)
