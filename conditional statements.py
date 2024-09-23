#if-elif-else(syntax)


#if
"""age= 21
if(age >= 18):
    print("can vote and applu for license")"""


#elif
light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

 #diff btwn if and elif   
num= 5
if(num>2):
    print("greater than 2")
elif(num>3):
    print("greater than 3")


#else
light = "pink"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken") #the space is called indentation

print("end of code")

marks = int(input("enter student marks: "))
if(marks >=90):
    grade ="A"
elif(marks >=80 and marks<90):
    grade ="B"
elif(marks >=70 and marks<80):
    grade= "c"
else:
    grade="D"
print("grade of the student ", grade)

#nesting

age= 34
if(age>= 18):
    if(age>=80):
        print("cannont drive")
    else:
        print("can drive")
else:
    print("cannot drive")
    