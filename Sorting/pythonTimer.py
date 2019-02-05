from BubbleSort.bubbleSort import bubbleSort as B
import timeit as T

bigList = []

with open ('bigListOfInts.txt', 'rb') as f:
    bigList = f.readlines()

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(B,bigList)
    
T.timeit(wrapped,number=1)
