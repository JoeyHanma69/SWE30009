def swap(array, i, j):
# ORIGINAL CODE:
 #    tmp = array[i]
# MODIFIED TO:
    tmp=array[k]
    array[i] = array[j]
    array[j] = tmp

def bubblesort(array):
    n = len(array)-1
    for i in range(0, len(array)):
        for j in range(0, n):
            if array[j] > array[j+1]:
                swap(array, j+1, j)
        n -= 1

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    bubblesort(array)
    print(array)

