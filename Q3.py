def fibonacci(n, mem={}):
    if type(n) != int:
        # msut be an integer
        return "Input must be an integer."
    elif n in mem:
        # returns value of stored values rather than repeating the same sequence 
        return mem[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        # For positive numbers: F(n) = F(n-1) + F(n-2); and store the sequence
        mem[n] = fibonacci(n - 1) + fibonacci(n - 2)
    else:
        # For negative numbers: F(-n) = (-1)^(n+1) * F(n); and store the sequence
        mem[n] = int((-1) ** (n + 1) * fibonacci(abs(n)))
    return mem[n] # returns the value of the last key i.e. n
    
print(fibonacci(100))


# For efficiency, let's take for example if n = 5:

# 5 --> 4 --> 3 --> 2 --> 1 = 1
# 		              --> 0 = 0 
# 	            --> 1 = 1			(repeated sequence)
# 	      --> 2 --> 1 = 1			(repeated sequence)
# 	            --> 0 = 0			(repeated sequence)
#   --> 3 --> 2 --> 1 = 1			(repeated sequence)
# 	            --> 0 = 0			(repeated sequence)
#   	  --> 1 = 1			        (repeated sequence)

# When n is 5, result is (1 + 0 + 1 + 1 + 0 + 1 + 0 + 1) = 5
# But if the first sequence could store the sequence values in a dictionary then 
# the rest of the iterations would just need to retrieve the values rather than 
# repeating the recursions hence the use of mem (memoization) to store the values 
# saving time and resources.