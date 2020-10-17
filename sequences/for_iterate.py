# how can we use a for loop to do what we did in while_iterate?

todo_list = ["clean room", "take out trash", "grocery shopping", "laundry"]

# todo is a variable we created on a fly and it refers to each value in todo_list.
for todo in todo_list:
    # we are able to pass todo here because we established it in the beginning of the for loop
    print(todo)


# if you don't need to know the index or how many items in a list, you can just print it out using this.

# if you want there to be a counter it can be done like this:

count = 1  # we have the count start at one because the first item can be represented as 1
for todo in todo_list:  # part of the reason why the count doesn't have to start at 0 is because the for loop will iterate over every value which is why we can have 1 to represent the 0 index.
    print("%d: %s" % (count, todo))  # print statement
    # incrementer, the incrementor here is used to list out the numbers. in the while loop it was also used to have the loop move through the list.
    count += 1

# notice how it is a bit different from the while loop.
