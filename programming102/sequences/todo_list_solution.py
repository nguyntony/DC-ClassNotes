todos = []

# Prompt the user the first time
new_todo = input("What do you need to do? ")
while len(new_todo) > 0:  # here we pass the condition that if the len of new_todo is greater than zero. we return a string but len returns an int which we can than use to compare to 0. this is why it does not raise an error.
    todos.append(new_todo)

    # Print the current list of to-do items
    print("To do:")
    print("====================")
    count = 1
    for todo in todos:
        print("%d: %s" % (count, todo))
        count += 1

    # Prompt the user again
    print("\n")
    new_todo = input("What do you need to do? ")

print("Have a nice day!")
