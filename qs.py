import random
from random import randint

def qs(a):
    if len(a) <= 1:
        return a
    p = random.choice(a)
    return qs([x for x in a if x < p]) + [x for x in a if x == p] + qs([x for x in a if x > p])

def quickSelect(arr, k):
    return select(arr, 0, len(arr) - 1, k)

def select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivotIndex = arr[randint(left,right)]
    pivotIndex = partition(arr, left, right, pivotIndex)
    if k == pivotIndex:
        return arr[k]
    elif k < pivotIndex:
        return select(arr, left, pivotIndex - 1, k)
    else:
        return select(arr, pivotIndex + 1, right, k)

def partition(arr, left, right, pivotIndex):
    pivot = arr[pivotIndex]
    arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
    storeIndex = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
            storeIndex += 1
    arr[right], arr[storeIndex] = arr[storeIndex], arr[right]
    return storeIndex




myArr = [x for x in range(20)]
random.shuffle(myArr)
print(myArr)
kth = quickSelect(myArr, 10)
print(kth)
# print(qs(myArr))
