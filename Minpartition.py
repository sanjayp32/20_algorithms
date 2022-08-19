#st->sumtotal,sc->sumCalculated
def Minpart2(arr,i,sc,st):
	if (i == 0):
		return abs((st-sc)-sc)
	return min(Minpart2(arr,i-1,sc+arr[i-1],st),Minpart2(arr,i-1,sc,st))
def Minpart(arr, n):
	st=0
	for i in range(n):
		st += arr[i]
	return Minpart2(arr,n,0,st)

arr =list(map(int,input("Enter the numbers : ").split(",")))
n = len(arr)
print("The minimum difference between two sets is ",Minpart(arr, n))
