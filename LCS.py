def Lcs(A,B,m,n):
    if m==0 or n==0:
        return 0
    elif A[m-1]==B[n-1]:
        return 1+Lcs(A,B,m-1,n-1)
    else:
        return max(Lcs(A,B,m-1,n),Lcs(A,B,m,n-1))
A=str(input("Enter first string : "))
B=str(input("Enter second string : "))
print("The Longest common subsequence is ",Lcs(A,B,len(A),len(B)))
