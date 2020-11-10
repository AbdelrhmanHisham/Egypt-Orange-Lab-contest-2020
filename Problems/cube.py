import math
num_of_testcases = input()
num_of_testcases = int(num_of_testcases)
test_cases = []
for num in range(num_of_testcases):
    test_cases.append(int(input()))


for edge in test_cases:
    print(int(math.sqrt(edge/6)))





