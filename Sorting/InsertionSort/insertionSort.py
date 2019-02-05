def insertionSort(A):
    for i in range(len(A)):
        current = A[i]

        j = i-1
        while j >= 0 and current < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current

    return A
