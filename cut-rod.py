def cut_rod(p, n):
    r = []
    for i in range(0, n+1):
        print(i, n)
        r.append(-1000000000)
    
    for i in range(0,n+1):
        cut_rod_2(p, n, r)

def cut_rod_2(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -10000000
        for i in range(0, n):
            q = max(q, p[i] + cut_rod_2(p, n-i,r))
    r[n] = q
    return q

def main():
    p = [1,3,5,10,13,16]
    n = 5

    result = cut_rod(p,n)
    print(result)

# A Naive recursive solution  
# for Rod cutting problem 
import sys 
  
# A utility function to get the 
# maximum of two integers 
def max(a, b): 
    return a if (a > b) else b 
      
# Returns the best obtainable price for a rod of length n  
# and price[] as prices of different pieces 
def cutRod(price, n): 
    if(n <= 0): 
        return 0
    max_val = -sys.maxsize-1
      
    # Recursively cut the rod in different pieces   
    # and compare different configurations 
    for i in range(0, n): 
        max_val = max(max_val, price[i] + 
                      cutRod(price, n - i - 1)) 
    return max_val 
  
# Driver code 
arr = [1, 5, 8, 10, 11, 15, 19, 20] 
size = len(arr) 
print("Maximum Obtainable Value is", cutRod(arr, size)) 
  
# This code is contributed by 'Smitha Dinesh Semwal' 
