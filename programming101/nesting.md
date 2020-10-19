# Nesting

- when you nest something, you are taking a piece of code and you are inserting it into another piece of code. 

```python
name = input("What is your name? ")

if len(name) > 3:
    # if the length of name is longer than 3 characters then this code block will run.
    print("Your name is long enough.")
    if len(name) > 15:
        # this if statement is nested inside of the if statement. this will also run and the condition will take name again and check if it is longer than 15 characters.
        # if this is true then this will code block will run.
        print("That's way too long partner.")
    else:
        # if it is not longer than 15 characters then this will run.
        print(f"Welcome {name}.")
else:
    # if the name is not longer than 3 characters then this code block will run.
    print("%s is too few characters." % len(name))
```

We are using the len() with a string to see how long the string is.

## Operators 
- and 
    - both conditions have to be true in order for the code block to run.
    ```python
    if True and True:
        print("Both conditions are true, this will run!")
    
    if True and False:
        print("This will not run!")
    ```
- or 
    - as soon as any condition is true when using or, the code block will run.
    ```python
    if False or True:
        print("This will because at least one of the conditions are true.")
        ```
