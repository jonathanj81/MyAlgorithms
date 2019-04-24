from BubbleSort.bubbleSort import bubbleSort as B
from SelectionSort.selectionSort import selectionSort as S
from InsertionSort.insertionSort import insertionSort as I
from MergeSort.mergeSort import mergeSort as M
from QuickSort.quickSort import quickSort as Q
from HeapSort.heapSort import heapSort as H
import timeit as T

bigList = []
mediumList = []
smallList = []

with open ('bigListOfInts.txt', 'rb') as f:
    bigList = map(int, f.readlines())
    
with open ('mediumListOfInts.txt', 'rb') as f:
    mediumList = map(int,f.readlines())
    
with open ('smallListOfInts.txt', 'rb') as f:
    smallList = map(int, f.readlines())

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


wrapped = wrapper(H,smallList)

print 'heapsort - smallList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(H,mediumList)

print 'heapsort - mediumList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(H,bigList)

print 'heapsort - bigList'
print T.timeit(wrapped,number=1)
print '---------'
