numbers = [1,2,3,4,5,6,7,8,9,10]

amazon_cart = ['notebooks','sunglasses','toys','grapes']
# print(amazon_cart)


# list-slicing is used to make copy of one list to another
# ls1 = ls2 -> ls1 will store the memory reference of ls2 -> to modify

# actions with lists
# len()
# adding
# append() -> append at last
# insert() -> insert at position
# extend()

# removing
# pop() -> removes last item
# remove() -> to remove a value from list,where as pop() remove by index.
# clear()

amazon_cart.append("Books")
# print(amazon_cart.index('Books'))
# print(amazon_cart)

# diff b/w sort() and sorted()
# sorted will return a new list
# sort() will modify the old list


# list-unpacking
num1,num2,num3,*others = [1,2,3,4,5,6,7,8,9,10]
# print(others)

weapons = None
# print(weapons)