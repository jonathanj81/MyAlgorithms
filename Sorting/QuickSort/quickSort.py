def quickSort(A, low=0, high=-1):
    if high == -1:
        high = len(A)-1

    if low < high:
        x,y,z = A[low],A[high],A[(low+high)/2]
        p = x <= y <= z and high or (y <= x <= z and low or (low+high)/2)

        pivot = A[p]
        A[low],A[p] = A[p],A[low]
        border = low

        for i in range(low+1,high+1):
            if A[i] < pivot:
                border += 1
                A[i],A[border] = A[border],A[i]
        A[low],A[border] = A[border],A[low]
        quickSort(A,low,border-1)
        quickSort(A,border+1,high)

    return A
