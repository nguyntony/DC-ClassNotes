# create a todo list program.

# ask the user if they want to add something to their list.
# if they hit enter, an empty string, then this will exit the program.
# I need to create a loop to iterate through the list

todo_list = []
index = 0
count = 1

# initial ask, not necessary but I like it
first = input("Add a task: ")
todo_list.append(first)

# while loop to ask the user
while first:
    add_list = input("Add another task: ")
    if add_list != "":
        todo_list.append(add_list)
    else:
        break

if todo_list == []:
    print("You have no tasks!")
else:
    print("Here is your todo list.")
    for todo in todo_list:
        print("%d: %s" % (count, todo))
        count += 1
