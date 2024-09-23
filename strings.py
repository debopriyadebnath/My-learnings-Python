"""str1 = "This is a string."
str2 = 'helloworld'
str3 =  ""this is a string""

str4 = "this is a string.\n we are creating it in python" #next line using escape sequence character
print(str4)
"""


#concatenation
"""str5 = "hello"
str6 = "world"
print (str5 + str6)"""


#length of str
"""str7= "debopriya"
print(len(str7))
"""

str8= "debopriya"
len1= len(str8)
print(len1)

str9= "debnath"
len2= len(str9)
print(len2)

final_str= str8+ " "+str9
print(final_str)
print(len(final_str))


#indexing
str = "debopriya"
ch = str[0]
print(ch) 


#slicing(accessing parts of a strings)(str[starting_idx:ending_idx])
#ending idx is not included
str= "Apna college"
print(str[1:4])
print(str[ :4]) #[0:4]
print(str[4: ]) #[5:len(str)]

#negative idx
str = "apple"
print(str[-3:-1])

#str functions

str.endswith #return true if string ends with substr
str = "im debopriya debnath"
print(str.endswith("ath"))

str.capitalize #capitalizes 1st char
str = "debopriya debnath"
print(str.capitalize())

str.replace #replaces all occurrences of old
str = "im debopriya debnath"
print(str.replace("d", "a"))

str.find #return 1st index of 1st occurrer
str= "i am debopriya debnath"
print(str.find("o"))

str.count #counts the occurences of subst
str= "i am debopriya debnath"
print(str.count("de"))
