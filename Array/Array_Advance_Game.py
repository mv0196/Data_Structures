def array_advance_game(arr):
    furtherest_reached=0
    for i in range(len(arr)):
        if i>furtherest_reached:
            return False
        furtherest_reached=max(furtherest_reached,i+arr[i])
        print(i,arr[i],furtherest_reached)
    #print(furtherest_reached)
    return furtherest_reached>=(len(arr)-1)

print(array_advance_game([3, 2, 0, 0, 2, 0, 1]))
print(array_advance_game([3,3,1,0,2,0,2]))
