## Functions

- self contained piece of code that preforms a repeatable task. 

### How to create a function?
``` python
def my_function():
    # code block

```
- use the "def" and you pass a function name which is similar to creating a variable

``` python
def my_function():
    print("Hi there, this print statement is inside of a function!")

def greet():
    print("Hi user!")
```

### Calling a function

- if you run your code after defining your functions you have to call them. 

``` python
def greet():
    print("Hi user!")

greet()
# Output: Hi user!
```

### Arguments
- arguments are values that you pass into a function so that the function can do whatever it received.

``` python
print("Hi there.")
```
- the string "Hi there." is an argument that you give to the print function. 

``` python
def join_string(a, b):
    print(a + " " + b)

b = input("What is your name?")
join_string(a, b)
# Output: Hi {name}
```
### Parameters
- parameters are the arguments that you define a function with. 

### Return
- a return value is given back from a function and we can use that return value to do something. 

``` python
def add_num(a, b):
    result = a + b
    return result
```
- if we run this function it will not print anything to the console, it will return the value "result" but it didn't print or anything. 

- return can be implicit or explicit 
    - implicit return is always none. 
    - if you do not establish a return statement then it will always return none. 
    - explicit return is when there is a return statement that has a value. 
    - if it does not have an explicit return statement then it has an implicit return none. 
- you can also return nothing 
- return exits the function, anything after the return statement will never be executed.
- you can return any data type. 