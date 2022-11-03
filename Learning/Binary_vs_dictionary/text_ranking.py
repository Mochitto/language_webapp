import time

# ************************************ SETUP ************************************
with open("google-10000-english.txt", "r") as text:
    original_array = [line for line in text.read().split("\n")]

# ************************************ FUNCTIONS ************************************
def binary_search(word, array):
    left = 0
    right = len(array) - 1
    mid = 0
    while left <= right:
        mid = (left + right)//2
        mid_word = sorted_array[mid]
        if word < mid_word:
            right = mid - 1
            continue 
        elif word > mid_word:
            left = mid + 1
            continue
        else:
            return mid 
    return False

def create_twin_lists(array):
    index_array = []
    sorted_array = sorted(array)
    for item in sorted_array:
        index_array.append(original_array.index(item))
    return sorted_array, index_array

# ************************************ Test area ************************************
sorted_array, index_array = create_twin_lists(original_array)

# Time for binary search O(logn)
start_time1 = time.time()
index_array[binary_search("the", sorted_array)]
print(f"Binary search finished in {time.time() - start_time1}")


dictionary_frequency = {index:word for (word, index) in enumerate(original_array)}

# Time for dictionary lookup O(1)
start_time2 = time.time()
dictionary_frequency["the"]
print(f"Dictionary lookup finished in {time.time() - start_time2}")