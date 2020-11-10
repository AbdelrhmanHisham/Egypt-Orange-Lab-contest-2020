import math
#Get the input numbers from user
#n,k = input().split()  
user_input = input()
input_list = user_input.split(' ')
#start with num greater than n
num = int(input_list[0])
k = int(input_list[1])
if(num%k == 0):
    num+=k
else : 
    num = math.ceil(num/k) * k

print(num)
