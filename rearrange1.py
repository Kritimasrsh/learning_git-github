# Rearrange - File 1
# Basic rearrangement functions

def sort_list(items):
    """Sort a list in ascending order"""
    return sorted(items)

def reverse_list(items):
    """Reverse a list"""
    return list(reversed(items))

if __name__ == "__main__":
    data = [5, 2, 8, 1, 9]
    print("Original:", data)
    print("Sorted:", sort_list(data))
    print("Reversed:", reverse_list(data))