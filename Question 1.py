# Joseph Pietroluongo 
# 1  Print the number of integers in an array that are above the given input and the number that are below, 
# e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

# hard coded array and number to compare
list1 = [1, 5, 2, 1, 10]
numbercheck = 6

#iterates through the array and compares each value
for i in range(len(list1)):
   
    if numbercheck < list1[i]:
        print("below: ",list1[i])
    
    elif numbercheck > list1[i]:
        print("above: ",list1[i])