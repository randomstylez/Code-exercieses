# Joseph Pietroluongo 
# Rotate the characters in a string by a given input and have the overflow appear at the beginning,
# e.g. “MyString” rotated by 2 is “ngMyStri”.

#hard coded string and number to rotate by
string1 = "MyString"
n = 2

def rotation(input,n):
    #gets the array from 0 to legnth - n
    first = input[0 : len(input)-n ] 
    #gets the array from legnth -n to legnth of the array
    second = input[len(input)- n : ] 
    #Combines the 2 arrays in the desired order.
    output1 = (second + first)
    print("{} rotated by {} is {}".format(string1, n, output1) )


if __name__ == "__main__": 
    rotation(string1,n) 