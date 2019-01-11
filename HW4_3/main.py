import random, mergeSort, countSort, QuickSort, os
from time import time
import sys



def main():
#This is for numbers between 0 and 100,000
    os.system("cls")
    sys.setrecursionlimit(5000)
    sortThis = []
    for _ in range(1000000):
        sortThis.append(random.randint(0,100000))
    sortThis2 = sortThis.copy()
    sortThis3 = sortThis.copy()
    max_val = max(sortThis3)
    length = len(sortThis2)-1
    t0 = time()
    mergeSort.mergeSort(sortThis)
    t1 = time()
    QuickSort.qsortIter(sortThis2, 0, length)
    t2 = time()
    countSort.countSort(sortThis3, max_val)
    t3 = time()

    mergeHunThousTime = t1-t0
    quikHunThousTime = t2-t1
    countHunThousTime = t3-t2

    print("This is with #'s between 0 and 100,000 \n")
    print("mergeSort took: " + str(mergeHunThousTime))
    print("quickSort took: " + str(quikHunThousTime))
    print("countSort took: " + str(countHunThousTime))

#This is for numbers between 0 and 5
    sortShort = []
    for _ in range(1000000):
        sortShort.append(random.randint(0,5))
    sortShort2 = sortShort.copy()
    sortShort3 = sortShort.copy()
    max_val = max(sortShort3)
    length = len(sortShort2)-1
    t0 = time()
    mergeSort.mergeSort(sortShort)
    t1 = time()
    QuickSort.qsortIter(sortShort2, 0, length)
    t2 = time()
    countSort.countSort(sortShort3, max_val)
    t3 = time()

    mergeFiveTime = t1-t0
    quickFiveTime = t2-t1
    countFiveTime = t3-t2

    print("\nThis is with #'s between 0 and 5 \n")
    print("mergeSort took: " + str(mergeFiveTime))
    print("quickSort took: " + str(quickFiveTime))
    print("countSort took: " + str(countFiveTime))

    print("\nmergeSort was the slowest and had a " + str(mergeHunThousTime/mergeFiveTime) + " times increase.")
    print("\nquickSort was in the middle and was  " + str(quikHunThousTime/quickFiveTime) + " times faster,\n\t but would only work with an iterative version.  When the numbers were changed from 0-100,000 to 0-5\n\t the recursive version got blown out")
    print("\ncountSort was by far the fastest and expierenced a: " + str(countHunThousTime/countFiveTime) + " times increase.")
    print("\ncountSort was " + str(mergeFiveTime/countFiveTime) + " times faster than mergeSort")
    print("\ncountSort was " + str(quickFiveTime/countFiveTime) + " times faster than quickSort")


main()
