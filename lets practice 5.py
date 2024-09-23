#store following word meanings in a python dictionary
#table: "a piece of furniture", "list of facts and figures"
#cat : "a small animal"

dictionary= {
      "cat": "a small animal",
      "table": ["a piece of furniture", "list of facts and figures"]



}
print(dictionary)

#you are given a list of subjects for students. assume one clssroom is required for 1 subject. how many classroom are needed by all students.
##"python", "java", "c++", "python", "javascript","java","python","java","c++","c"

subjects = {
         "python","java", "c++", "python", "javascript",
         "java","python","java","c++","c"


}
print(subjects)
print(len(subjects))


#WAP to enter marks of 3 sunjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as key and marks as value

marks = {}

x= int(input("enter phy :"))
marks.update({"phy": x})

x= int(input("enter maths :"))
marks.update({"maths": x})

x= int(input("enter chem :"))
marks.update({"chem": x})

print(marks)



