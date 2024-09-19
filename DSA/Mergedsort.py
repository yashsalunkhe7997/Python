def mergedsort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    leftside=mergedsort(arr[:mid])
    rightside=mergedsort(arr[mid:])

    return merge(leftside,rightside)

def merge(left,right):
    merged=[]
    i=j=0
    while i < len(left) and j < len(right):
        if left[i]< right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j +=1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


arr=[50,60,10,45,60,12,3]
sort=mergedsort(arr)
print(sort)