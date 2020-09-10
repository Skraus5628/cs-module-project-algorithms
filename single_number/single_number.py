'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#to do:
# Loop over an array, check for duplicates, return numbers in array that are non duplicate

#Ideas: Dictionaries cannot have doubles
#Divide with sets?
#Loop over and use Count() 

def single_number(arr):
    # Your code here

    for num in arr:
        if arr.count(num) == 1:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")