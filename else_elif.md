# Else and Elif

When using if statements you are evaluating something.
```python
a = 1
if a == 1:
    print("Yes!")

if a == 0:
    print("No!")
```
## Elif
We can combine these together and have multiple conditions.

```python
a = 1
if a == 1:
    print("Yes!")
elif a == 0:
    print("No!")
```
Note how elif is at the same indentation as if.
___
When the expression is True then the code block will run, if it is False then it will not run.

When the if statement comes across a True condition it will run that code block and immediately exit.
```python
a = 1
if a == 1:
    print("Only this print statement will run.")
elif a >= 1:
    print("This will not run although it is true. The code has already exited the if statement.")
```
## Else

Else will not accept a condition like if and elif. 
Else is used as a final condition in the event that all other conditions are false. 

```python
a = 1

if a == 0:
    print("False, will not run.")
elif a == 5:
    print("False, will not run.")
elif a == 10:
    print("False, will not run.")
else: 
    print("All of the conditions are false, this will run.")
```