# Python has several built-in types of seguences, in this file we'll
# concentrates in lists type

# IMPORTANT
# The main difference between lists and tuples is that you can change a list,
# but you can’t change a tuple. A list might be useful if you need to add
# elements as you go along, while a tuple can be useful if, for some reason,
#  you can’t allow the sequence to change.

# List of movies
list_of_spanish_movies_in_73s = ['Anna and the Wolves', 'Habla, mudita',
                                 'The Girl from the Red Cabaret', 'La otra imagen', 'Queridísmos verdugos',
                                 'Return of the Blind Dead', 'The Spirit of the Beehive',
                                 'Lo verde empieza en los Pirineos']
# Printing a List of 73's of Spanish movies.
print(list_of_spanish_movies_in_73s)

# Common Sequence Operations
# Indexing - All elements in a sequence are numbered—from zero and upward.
# You can access them individually with a number. For exemple the second item
# on the list. Note: The first element of the list is the number 0 (zero)

print(list_of_spanish_movies_in_73s[1])  # Habla, mudita

# When you use a negative index, it counts from the right, from the last element.
print(list_of_spanish_movies_in_73s[-1])  # Lo verde empieza en los Pirineos

# Slicing - you can use slicing to access ranges of elements. You do this by
# using two indices, separated by a colon. The first index is the number of the
# first element you want to include and the last index is the number of
# the first element after your slice
print(list_of_spanish_movies_in_73s[2:5])  # ['The Girl from the Red Cabaret', 'La otra imagen', 'Queridísmos verdugos']

# Creating a list from a string
letters_of_name = list('Alexandre')
print(letters_of_name)

# Changing Lists: Item Assignments
x = [1, 1, 1]
x[1] = 2
print(x)

# Deleting Elements.
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)

# append - used to append an object to the end of a list.
names.append('Alexandre')
print(names)

# clear - clears the contents of a list, in place.
lst = [1, 2, 3]
print(lst)
lst.clear()
print(lst)
