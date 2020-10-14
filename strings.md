# Strings!

## There are several ways to make strings!
```python
'using single quotes'
"using doubles quotes"

'''
triple single quotes
which allows you to have a string span across multiple lines.
'''

"""
and you can do the same
with triple double quotes
"""
```

## Concatenation 
You can combine strings with one another using the ' + ' operator.
```python
"hi" + "there!" # note: this will result in hithere! no space is added!

"I" + " " + "want" + " " + "spaces!" # you'd have to do something like this to add spaces!
```
It is important to note that you can ' + ' strings but you cannot ' - ' strings.
```python
"hi there!" - "!" # error
```

## F - string
You can assign values to a variable and then later add that into a string.

```python
my_name = "Tony"
age = 24

print(f"Hi there! My name is {my_name} and I am {age} years old!")
# Hi there! My name is Tony and I am 24 years old!
```

## Interpolation
This is another way of inserting information into a string.
```python
my_name = "Tony"
age = 24

print("Hi there! My name is %s and I am %s years old!" % (my_name, age))
# Hi there! My name is Tony and I am 24 years old!
```
It's important to note that when passing on values into this string you have to put the variables in the precise order that you wish.

```python
my_name = "Tony"
age = 24

print("Hi there! My name is %s and I am %s years old!" % (age, my_name))
# Hi there! My name is 24 and I am Tony years old!
```
This output will switch the values and result in a different sentence.

## Escape sequence
```python
print("\tThis will give you a tab") 
#     This will give you a tab

print("This will\ngive you a new line") 
# This will
# give you a new line
```

