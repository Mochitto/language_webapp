# TODO: 
# def get_frequency_dictionary(language):
#      return

with open("google-10000-english.txt", "r") as text:
    original_array = [line for line in text.read().split("\n")]

dictionary_frequency = {index:word for (word, index) in enumerate(original_array)}

# TODO: make it so that this is the only function to export
# def get_frequency_mapping(file, lang_dictionary):
#     return

"""TODO
DONE - decide which data structure/algorithm to use 
- Create a dictionary that holds the frequency ranges categories
- Read text from file => split on every whitespace to have an array
- Get length of the words array
- Iterate over the words and count them, incrementing the frequency ranges dictionary' matching values
- Return the frequency dictionary
"""
# EXTRA FEATURE/FUTURE TODO: check another text file (known words) and create a function that returns the % of known words
# How to make this work with just one iteration? 