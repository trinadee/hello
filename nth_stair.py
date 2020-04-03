# A program to count the number of ways to reach n'th stair 
  
# Recurssive program to find n'th fibonacci number 
def fib(n): 
    if n <= 1: 
        return n 
    return fib(n-1) + fib(n-2) 
  
# returns no. of ways to reach s'th stair 
def countWays(s): 
    return fib(s + 1) 
  
# Driver program 
  
s = 7
print("Number of ways = ", countWays(s)) 
  
# Contributed by Harshit Agrawal 
