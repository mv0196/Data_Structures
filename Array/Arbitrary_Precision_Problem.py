def plus_one(arr):
    '''
    i=len(arr)-1
    sum=arr[i]+1
    rem=sum%10
    carry=sum//10
    arr[i]=rem
    while carry>0 and i>0:
        i-=1
        sum=arr[i]+carry
        rem=sum%10
        carry=sum//10
        if i==0:
            arr[i]=rem
            arr=[carry]+arr
        else:
            arr[i]=rem
    return arr
    '''
    arr[-1]+=1
    for i in reversed(range(1,len(arr))):
        #print(i)
        if arr[i]!=10:
            break
        arr[i]=0
        arr[i-1]+=1
        #print(i,arr[i],i-1,arr[i-1])
    if arr[0]==10:
        arr[0]=1
        arr.append(0)
    return arr

print(plus_one([9,9,9]))
