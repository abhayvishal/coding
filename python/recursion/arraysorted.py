def isSorted(a,start=0):
    l=len(a)
    if(start==l or start==l-1):
        return True

    if a[start]>a[start+1]:
        return False
    start = start+1
    return isSorted(a[start:])

a=[1,2,3,4,5,6,7]
print(isSorted(a))