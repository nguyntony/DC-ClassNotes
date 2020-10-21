## Iterate through lists

``` python
pets = ["dog", "cat", "bird", "fish"]
```

## Using a while loop
``` python
index = 0 

while index < len(pets):
    print(index + 1, pets[index])
    index += 1
``` 
- len() returns an integer
    - which is why you don't get an error when you compare the list with an integer. 

## Using a for loop
``` python
for idx, pet in enumerate(pets):
    print(idx, pet)
    
```
- for loop:
    - the for loop declaration creates a variable and then assigns each item in the list and passes it to that variable.
    - in the code block we are then using that variable and using it for a print statement.
    - each time the for loop passes over an item, it is essentially reassigning the variable.

- enumerate:
    - if we wanted to list the index with the item.
    - we assign another variable that holds the index. 