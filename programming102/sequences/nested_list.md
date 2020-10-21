## Nested Lists

``` python
siblings = [
    ["Michelle", "Nguyen", 19],
    ["Misty", "Nguyen", 15]
]
```
### Accessing nested lists
- in nested lists
    - you can add another [] 
    - siblings[index][index]

``` python
print(siblings[0][2])
# Output: 19
```

### Using variables
- you can store ways of accessing a nested list in a variable to make it easier to read
``` python
siblings = [
    ["Michelle", "Nguyen", 19],
    ["Misty", "Nguyen", 15]
]

oldest_sister = siblings[0]
youngest_sister = siblings[1]

youngest_sister[2] = 16
```
### Loop through a nested list 
- you used a nested for loop!
``` python
for sister in siblings:
    print("First", "Last", "Age")
    for attribute in sister:
        print(attribute)
```
- reads as:
    - for each item in siblings
    - here we call each item, sister
    - we want to print first last and age
    - we also want to print something else using another for loop
        - the other for loop will read as:
            - for each sister in siblings we want to access each item of each sister 
            - and we want to print each item which we referred to them as attribute