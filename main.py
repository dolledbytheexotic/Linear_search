#The first line def function uses the term linear_search which calls items and list then we use a for loop in range from 0 to the number of items in list
def linear_search(list,target):
  for i in range (0,len(list)):
    if list[i]==target:
      return i
  return None
#We use a if statement to compare the i in for loop to target and if its equal to target we return none 


#In the second function we have verify which takes the place of result which uses the linear search function 


def verify(index):
  if index is not None: 
    print("Target is found at index",index)

  else :
    print("Target is not found in list")
#checks if numbers has the target and at what index and if it doesn't it prints "target is not found in list"

numbers=[1,2,3,4,5,6,7,8,9,10]

result=linear_search(numbers,9)
verify(result)