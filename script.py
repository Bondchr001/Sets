# ============================================
# Creating Sets
# ============================================

# Method 1: Using curly braces {}
fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # {'cherry', 'banana', 'apple'} - order may vary!

# Method 2: Using set() constructor
numbers = set([1, 2, 3, 2, 1])  # From a list
print(numbers)  # {1, 2, 3} - duplicates removed!

# Converting string to set (each character becomes an element)
letters = set('hello')
print(letters)  # {'h', 'e', 'l', 'o'} - only one 'l'!

# Creating an empty set
empty_dict = {}        # This is a DICTIONARY!
empty_set = set()      # This is a SET!

print(type(empty_dict))  # <class 'dict'>
print(type(empty_set))   # <class 'set'>
hobbies = {'basketball', 'football', 'video games'}
print(hobbies)

# Creating an empty set
empty_dict = {}        # This is a DICTIONARY!
empty_set = set()      # This is a SET!

print(type(empty_dict))  # <class 'dict'>
print(type(empty_set))   # <class 'set'>
# Demonstrating set characteristics
my_set = {3, 1, 4, 1, 5, 9, 2, 6}
print(my_set)  # {1, 2, 3, 4, 5, 6, 9} - sorted? No! Just happens to look that way

# Cannot index into a set
# print(my_set[0])  # TypeError: 'set' object is not subscriptable

# But you CAN iterate through a set
for num in my_set:
    print(num, end=' ')  # Prints each number (order not guaranteed)

# Fast membership testing - this is where sets SHINE!
print(5 in my_set)   # True - checked instantly!
print(10 in my_set)  # False

# Create a set of 5 numbers. Practice using add(), remove(), and discard().
# What happens when you try to remove something that isn't there?
numbers = set([1, 2, 3, 4, 5])
print(numbers)
numbers.remove(1)
print(numbers)
numbers.add(5)
print(numbers)
numbers.discard(5)

friend1 = ['Avatar','Titanic','Cars']
friend2 = ['Batman', 'Jaws','Avengers']
