from BubbleSort.bubbleSort import bubbleSort as B
from SelectionSort.selectionSort import selectionSort as S
import timeit as T

bigList = []

with open ('bigListOfInts.txt', 'rb') as f:
    bigList = f.readlines()

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(S,bigList)

print 'selection'
print T.timeit(wrapped,number=1)
print '---------'

wrapped = wrapper(B,bigList)

print 'bubble'
print T.timeit(wrapped,number=1)
print '---------'
