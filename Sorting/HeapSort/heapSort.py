def heapSort(A):

    def floatUp(pos):
        parent = (pos-1)/2
        if A[pos] > A[parent]:
            A[pos],A[parent] = A[parent],A[pos]
        if parent > 0:
            floatUp(parent)

    def bubbleDown(pos,n):
        top = pos
        left = 2*pos+1
        right = 2*pos+2
        if pos == 0:
            left,right = 1,2
        if left < n and A[left] > A[top]:
            top = left
        if right < n and A[right] > A[top]:
            top = right
        if top != pos:
            A[top], A[pos] = A[pos], A[top]
            bubbleDown(top,n)

    for i in range(len(A)-1,0,-1):
        floatUp(i)

    for i in range(len(A)-1,0,-1):
        A[i], A[0] = A[0], A[i]
        bubbleDown(0,i)
        
    return A
                               
            
            
        
