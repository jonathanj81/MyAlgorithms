from BubbleSort.bubbleSort import bubbleSort as B
from SelectionSort.selectionSort import selectionSort as S
from InsertionSort.insertionSort import insertionSort as I
from MergeSort.mergeSort import mergeSort as M
from QuickSort.quickSort import quickSort as Q
import timeit as T

bigList = []
mediumList = []
smallList = []

with open ('bigListOfInts.txt', 'rb') as f:
    bigList = f.readlines()
    
with open ('mediumListOfInts.txt', 'rb') as f:
    mediumList = f.readlines()
    
with open ('smallListOfInts.txt', 'rb') as f:
    smallList = f.readlines()

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


wrapped = wrapper(Q,smallList)

print 'quicksort - smallList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(Q,mediumList)

print 'quicksort - mediumList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(Q,bigList)

print 'quicksort - bigList'
print T.timeit(wrapped,number=1)
print '---------'
