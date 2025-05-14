# sets are unordered collection of unique items.

my_set = {1,2,3,4,5}
new_set = my_set.copy()
your_set = {4,5,6,7,8,9,10}


#  methods in sets
print(my_set.difference(your_set))
# difference_update() -> will remove the difference from the set
print(my_set.intersection(your_set))
# isdisjoint() -> will check if these two sets have anything in common.
print(my_set.union(your_set))
