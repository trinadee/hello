def cut(p,n):
    r = []
    s = []

    for i in range(0, n+1):
        r.append(-1)
        s.append(-1)
    print(r)
    print(s)
    for j in range(0,n):
        print("i ", j)
        q = -1000
        for k in range(0,j):
            if q < p[k] + r[j-k]:
                q = p[k] + r[j - k]
                s[j] = k
        r[j] = q

    while n>0:
        print(s[n-1])
        n = n - s[n-1]
        if s[n-1] == 0:
            break
    return r,s



def cut_rod(p,n):
    r = [-1]*(n+1)
    s = [-1]*(n+1)

    cut_rod_help(p,n,r,s)

    return r, s

def cut_rod_help(p,n,r,s):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1,n+1):
            temp = p[i] + cut_rod_help(p, n-i, r,s)
            if q < temp:
                q = temp
                s[n] = i
    r[n] = q

n = int(input('Enter the length of the rod in inches: '))
 
# p[i] is the price of a rod of length i
# p[0] is not needed, so it is set to None
p = [None]
for i in range(1, n + 1):
    price = input('Enter the price of a rod of length {} in: '.format(i))
    p.append(int(price))
 
r, s = cut_rod(p, n)
print('The maximum revenue that can be obtained:', r[n])
print('The rod needs to be cut into length(s) of ', end='')
while n > 0:
    print(s[n], end=' ')
    n -= s[n]
