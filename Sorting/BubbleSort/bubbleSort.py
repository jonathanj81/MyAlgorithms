def bubbleSort(A):

    for i in range(len(A)-1,0,-1):
        swapped = False

        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        if not swapped:
            return A

    return A
