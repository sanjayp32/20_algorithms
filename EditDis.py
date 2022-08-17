#Edit Distance
def Edis(str1,str2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        return Edis(str1,str2,m-1,n-1)
    return 1+min(Edis(str1,str2,m,n-1),Edis(str1,str2,m-1,n),Edis(str1,str2,m-1,n-1))
str1=str(input("Enter the string : "))
str2=str(input("Enter the string : "))
print(Edis(str1,str2,len(str1),len(str2)))