#print numbers from 1 to 100
i=1
while i<=100:
  print(i)
  i+=1

  
#print the numbers 100 to 1 
i= 100
while i >= 1: #stopping condn
  print(i)
  i -=1


#print the multiplication table of number n.
n = int(input("enter number:"))
i=1
while i <=10:
    print(n*i)
    i += 1


#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
#traverse
nums = [1,4,9,16,25,36,49,64,81,100]
idx= 0
while idx < len(nums):
   print(nums[idx])
   idx +=1


#search for a number x in this tuple using loop
(1,4,9,16,25,36,49,64,81,100,36)

x= 36
i= 0
while i < len(nums):   
    if(nums[i]==x):
       print ("FOUND at idx", i)
    else:
       print("finding...")
       i+=1