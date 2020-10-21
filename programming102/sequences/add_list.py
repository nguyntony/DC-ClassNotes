# how do you add items to a list?

todo_list = ["clean room", "take out trash", "grocery shopping", "laundry"]

"""
1. .append() - this adds individual items
2. concantenate two lists together
3. .extend() - use elements from another list.
"""

# .append()
# inside of the () in the .append() you can pass it a value and here we are passing in a string.
todo_list.append("walk dogs")
print(todo_list)
# notice that "walk dogs" will be added to the end of the list.

# concatenate lists
more_todo = ["mow lawn", "meal prep"]

todo_list = todo_list + more_todo

print(todo_list)
# notice that what get's added second will be added to the end of the first list.
# concatenation will produce a new list.

# .extend()

todo_list.extend(more_todo)
print(todo_list)
