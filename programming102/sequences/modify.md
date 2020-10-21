## Modifying lists

### Adding to a list
``` python
my_pets = ["Taro", "Mochi"]
```
#### Using append method
``` python
my_pets = ["Taro", "Mochi"]
my_pets.append("Appa")
```
- append:
    - print(my_pets.append("Appa")) 
    - does not return anything 

#### Concatenation
``` python
my_dogs = ["Taro", "Mochi"]
my_cats = ["Cat1", "Cat2"]

my_pets = my_dogs + my_cat
```
- this is will not modify the lists before.
- it will create a new list with the contents of the lists. 
- important to note that you can only concantenate lists. 
___



``` python
my_pets = my_dogs + []
```
WILL GET BACK TO THIS


#### Combined literal
``` python
combined_literal = [1, 2, 5] + [True, False, "hello"]
print(combined_literal)
```
- you don't have to store the list in a variable. 


#### Extend
``` python
num_list = [1, 2, 3]
alpha_list = ["a", "b", "c"]

num_list.extend(alpha_list)
```
- when using .extend, you are keeping the same list but modifying it.

#### Changing values inside of a list
``` python
my_pets = ["Taro", "Mochi", "Appa"]
my_pets[1] = "Baby Mochi"
```

#### Delete
``` python
del my_pets[0]
```