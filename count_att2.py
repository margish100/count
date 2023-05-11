'''
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773
'''

def solve(n):
    if n<4:
        return str(2**(n-1))+'/'+str(2**n)
    v1=2
    v2=1
    v3=1
    P = 4
    count = 8
    for i in range(4,n+1):
        temp= v3
        # print("result of temp",temp)
        v3=v2
        # print("result of v3", v3)
        v2=v1
        # print("result of v2", v2)
        v1=P
        # print("result of v1", v1)
        P= count
        # print("result of P", P)
        count = (count-temp)*2+temp
        # print("result of count", count)
    return str(v3+v2+v1)+'/'+str(count)

print(f"for 5 days: {solve(5)}")
print(f"for 10 days: {solve(10)}")