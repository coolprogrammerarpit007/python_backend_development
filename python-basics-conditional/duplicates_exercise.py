# Exercise:- Check for duplicates in the list.

some_list = ['a','b','c','b','d','m','n','n']

letter_frequency = dict()
duplicate_letters = list()
for letter in some_list:
    letter_frequency[letter] = letter_frequency.get(letter,0) + 1


for key in letter_frequency.keys():
    if letter_frequency[key] > 1:
        duplicate_letters.append(key)


print(duplicate_letters)