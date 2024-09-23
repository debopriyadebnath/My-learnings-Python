count = 1
while count <= 5:
    print("hello")
    count+=1

    #print numbers from 1 to 5
    i= 1
    while i <= 5:
        print(i)
        i+=1

        print("loop ended")
 
 #break and continue
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i +=1
print("end of loop")

#print odd num from 1 to 10
i= 1
while i<= 10:
    if(i%2==0):
        i +=1
        continue
    print(i)
    i += 1

#print even num from 1 to 10
i= 1
while i<= 10:
    if(i%2!=0):
        i +=1
        continue
    print(i)
    i += 1


#FOR loop (used for sequential traversal. for traversing list, string, tuples)
nums = [1,2,3,4,5]

for val in nums:
    print(val)

