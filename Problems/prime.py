
def is_prime_number(x):
    if x >= 2:
        for y in range(2,int(x/2)):
            if not ( x % y ):
                return False
    else:
	    return False
    return True

# def is_prime(n):

#     """
#     Assumes that n is a positive natural number
#     """
#     # We know 1 is not a prime number
#     if n == 1:
#         return False

#     # We store the number of factors in this variable
#     factors = 0
#     # This will loop from 1 to n
#     for i in range(1, n+1):
#         # Check if `i` divides `n`, if yes then we increment the factors
#         if n % i == 0:
#             factors += 1
#     # If total factors are exactly 2
#     if factors == 2:
#         return True
#     return False


list_of_prime = []


input_num = input()

upper = int(input_num)
lower = upper-2
if(upper != 2 and is_prime_number(lower)):
    print(2 , lower)
else:
    print(-1)
