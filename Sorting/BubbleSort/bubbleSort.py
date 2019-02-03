import cPickle as P
import timeit as T

def bubbleSort(A):

    for i in range(len(A)-1,0,-1):
        print ' -- '
        swapped = False

        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        if not swapped:
            return A

    return A

bigList = []

with open ('../bigListOfInts.pkl', 'rb') as f:
    bigList = P.load(f)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(bubbleSort,bigList)
    
T.timeit(wrapped,number=1)
