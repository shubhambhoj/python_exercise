def break_words(stuff):
    """ this function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)    
    print(word)

def sort_sentence(sentence):
    """ takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):  
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


"""
# please check exercise 25 

sentence = input("Enter any sentence.")

# calling break_words() fun
words = break_words(sentence)
print(words)

# calling sort_word() fun.
sorted_words = sort_words(words)
print(sorted_words)

# calling print_first_word() and print_last_word() with passing "words" variable
print_first_word(words)
print_last_word(words)
print(words)

# calling print_first_word() and print_last_word() with passing "sorted_words" variable
print_first_word(sorted_words)
print_last_word(sorted_words)
print(sorted_words)

# calling print_first_and_last() and print_first_and_last_sorted()
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)

sorted_words = sort_sentence(sentence)
print(sorted_words)                         # OR we can print(sort_sentence(sentence))

"""