count = dict()

def nth_most_rate_signature(list_nums, n):
 
    # Verifies if the list_nums is actually a list and the n is actually an integer
    if type(list_nums) is list and type(n) is int:

        # Stores the value in a dict using the key : list_num and value : appearance count  
        for value in list_nums:
            count[value] = count.get(value, 0) + 1
        
        # Sorts the list to start from the rarest order 
        list_nums = sorted( [ (value, key) for key, value in count.items() ])
        # print(list_nums)

        # Incase n is greater than our options
        if n > len(list_nums):
            print("n is out of range abeg")
        else:
            # -1 from n, considering list start from 0
            n -= 1 
            rarest = list_nums[n]

            # answer
            print(rarest[1])

    # If verification @line 6 fails
    else:
        print('''   
    ========== Error Message =============
        Please crosscheck your values
            list_nums = list(), n = integer()
        ''')
    

# Calling and passing values to the function 
list_nums = [5,4,5,4,5,4,4,5,3,3,3,2,2,1,5]
nth_most_rate_signature(list_nums, "Today")


