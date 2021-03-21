#create a program for merge sort
user_input=input("Enter the elements of array:").split(",")
alist=[int(i) for i in user_input]
print("Given array is:")
print(alist)
le=len(alist)-1
def merge(a:list,start:int,mid:int,end:int):
    n1=mid-start+1
    n2=end-mid
    l=[None]*n1
    r=[None]*n2
    k=0
    # making temp list to store two sorted list
    for i in range(n1):
        l[i]=a[start+i]
    for j in range(n2):
        r[j]=a[mid+1+j]
    while(i<=mid and j<=end):
        if l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1
    if (i>mid):
        while(j<=end):
            
            a[k]=r[j]
            
            j+=1
            k+=1
    else:
        while(i<=mid):
            a[k]=l[i]
            i+=1
            k+=1
    a=b.copy()
    return a
    
    
def mergeSort(a:list,start:int,end:int):
    if(start<end):
        mid=(start+end)//2
        mergeSort(a,start,mid)
        mergeSort(a,mid+1,end)
        merge(a,start,mid,end)
    return a
print(mergeSort(alist,0,le))