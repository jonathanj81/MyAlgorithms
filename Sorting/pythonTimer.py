from BubbleSort.bubbleSort import bubbleSort as B
from SelectionSort.selectionSort import selectionSort as S
from InsertionSort.insertionSort import insertionSort as I
from MergeSort.mergeSort import mergeSort as M
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


wrapped = wrapper(M,smallList)

print 'merge - smallList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(M,mediumList)

print 'merge - mediumList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(M,bigList)

print 'merge - bigList'
print T.timeit(wrapped,number=1)
print '---------'
