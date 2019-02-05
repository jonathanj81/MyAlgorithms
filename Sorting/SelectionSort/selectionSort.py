def selectionSort(A):
    for i in range(len(A)):
        mindex = i
        for j in range(i+1,len(A)):
            if A[j] < A[mindex]:
                mindex = j

        A[i],A[mindex] = A[mindex],A[i]

    return A
