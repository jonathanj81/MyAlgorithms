from BubbleSort.bubbleSort import bubbleSort as B
from SelectionSort.selectionSort import selectionSort as S
from InsertionSort.insertionSort import insertionSort as I
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

wrapped = wrapper(I,smallList)

print 'insertion - smallList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(S,smallList)

print 'selection - smallList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(B,smallList)

print 'bubble - smallList'
print T.timeit(wrapped,number=1)
print '---------'


wrapped = wrapper(I,mediumList)

print 'insertion - mediumList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(S,mediumList)

print 'selection - mediumList'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(B,mediumList)

print 'bubble - mediumList'
print T.timeit(wrapped,number=1)
print '---------'
