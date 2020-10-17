# how to iterate through a list?

todo_list = ["clean room", "take out trash", "grocery shopping", "laundry"]

index = 0  # begin at 0
# condition: while index is less than the length of todo_list. this will allow us to loop through all the values in this list.
while index < len(todo_list):
    # we are creating a variable which refers to each single value in the list. we pass [index] bc it will change with each loop.
    todo = todo_list[index]
    # a print statement that we want to do. using string interpolation we are adding 1 so that the first item in our list will be 1 and we are passing on the variable that we established earlier.
    print("%d: %s" % (index + 1, todo))
    index += 1  # we want to increment the index so that we are actually going through the loop
