# User Input

- You can ask for user input by using the input() function. 
- A window will pop up and wait for a response from the user before continuing with the code, this is called blocking. 
- IMPORTANT: When using input what the user returns it will be a string.



```python
your_name = input("What is your name? ")

fav_num = input("What is your favorite number? )
# user gives the value 10
fav_num = "10"
# this 10 is a string not an integer
```
- We are asking the user for their name.
- We can pass that value and store it into a variable. 

```python
your_name = input("What is your name? ")
print(f"I think your name is {your_name}")
```

