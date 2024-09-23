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
print(student)
print(student.keys())


print(list(student.keys()))