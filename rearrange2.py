# Rearrange - File 2
# Advanced rearrangement utilities

def shuffle_list(items):
    """Shuffle a list randomly"""
    import random
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

def bubble_sort(items):
    """Bubble sort implementation"""
    arr = items.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22]
    print("Original:", data)
    print("Shuffled:", shuffle_list(data))
    print("Bubble sorted:", bubble_sort(data))