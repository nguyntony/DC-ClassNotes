## List Comprehension

``` python
num_list = [1, 2, 3]
print([num for num in num_list])
```
- we write the for loop but we wrap it around a list.
- and before the for loop we write out the variable we give/pass into the for loop, in this case it is num.
- so what this does is that it takes the num returns it in a list. 
- instead of created an empty list then appending the return value into that empty list, we can do it like this as a shorthand.

``` python
num_list = [1, 2, 3]
factor = 2

print([num * factor for num in num_list])
```
- we created the for loop and passed it the num variable
- before the for loop we can use the num variable 
- we want to manipulate the variable by multiplying it with the factor. 