# -*- coding: utf-8 -*-
import random
import timeit


#### SORTOWANIE HEAPSORT
# step 1: construct heap tree
# step 2: delete root node and replace with last leaf node of tree
# step 3: heapify tree
# For a heap, the children of an element n are at index 2n+1 for the left child and 2n+2 for the right child.


def heapSort(data):
    dataSize = len(data)

    def swap(parent_idx, child_idx):
        if data[parent_idx] < data[child_idx]:
            data[parent_idx], data[child_idx] = data[child_idx], data[parent_idx]

    def indexing(parent_idx, unsortedData):

        greaterElement_idx = lambda a, b: a if data[a] > data[b] else b

        while parent_idx * 2 + 2 < unsortedData:
            childLeft_idx = parent_idx * 2 + 1
            childRight_idx = parent_idx * 2 + 2
            greaterChild_idx = greaterElement_idx(childLeft_idx, childRight_idx)
            swap(parent_idx, greaterChild_idx)
            parent_idx = greaterChild_idx

    def convert_to_heap():
        for element in range((dataSize/2)-1, -1, -1):
            indexing(element, dataSize)

    def sorting():
        iter = dataSize
        while iter > 0:
            iter -= 1
        swap(iter, 0)
        indexing(0, iter)

    convert_to_heap()
    sorting()


# generowanie danych
data = []
a = range(0, 1000)
for i in range(0, 2000):
    data.append(random.choice(a))

# sprawdzenie wydajności kodu
start_time = timeit.default_timer()
heapSort(data)
print(timeit.default_timer() - start_time)





