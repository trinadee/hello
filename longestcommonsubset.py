def LCS(S1, S2, m, n):
    if m == 0 or n == 0:
        return 0;
    elif S1[m-1] == S2[n-1]:
        return 1+ LCS(S1, S2, m-1, n-1)
    else:
        return max(LCS(S1, S2, m, n-1), LCS(S1, S2, m-1, n))
    #print("True")

def main():
    s1 = 'AGHT'
    s2 = 'GHT'
    print("Length of LCS is ", LCS(s1, s2, len(s1), len(s2)))


main()
