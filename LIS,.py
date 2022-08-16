global maximum
def lis2(arr, n):
	global maximum
	if n == 1:
		return 1
	m= 1
	for i in range(1, n):
		res = lis2(arr, i)
		if arr[i-1] < arr[n-1] and res+1 > m:
			m = res + 1
	maximum = max(maximum,m)
	return m
def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1
    lis2(arr, n)
    return maximum	
arr=list(map(int,input("Enter the numbers : ").split(",")))
print ("Length of lis is ", lis(arr))

