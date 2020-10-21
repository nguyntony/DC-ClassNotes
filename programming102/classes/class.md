## Class

``` python
class Person:
    pass
```
- create a class by stating the class keyword. 

``` python
tony = Person()
```
- instantiate a type class by assigning a variable to the class you created. 
    - instantiate means creating a self contained instance of a class. 

- you can define functions inside of classes.

``` python 
class Person:
    def __init__(self):
        print("You created a new instance of Person.")
```

- __init__ this is a function that we created inside of the Person class will run everytime you instantiate a class but will not run when you are doing something with the class.
    - this function runs automatically. 

- self: this goes inside of the parameters of the __init__
    - it is the first parameter inside of every method]
    - what is self referring to? well it is referring to itself. 
    - self is the standard however you could rename it something else like foo but it will still work like self. although you are naming it something else, its functionality is the same.
    - self is referring to the instance of that class object.  

### Attributes
- values in a class that can be accessed using the attribute name. 

``` python
class Person:
    def __init__(self):
    self.name = "Tony"
    self.age = 24

tony = Person()
print(tony.age)
```
- you access the age by using the instance name and .age 
- this isn't really reusable though.

``` python
class Person:
    def __init__(self, name, age):
    self.name = name
    self.age = age

tony = Person("tony", 24)
tyler = Person("tyler", 24)

print(f"Hi {tony.name} you are {tony.age} years old.")
# Output: Hi tony you are 24 years old. 
```
- setting your class up like this will make it act more like blueprint and it is reusable. 

### Default parameters
``` python
class Person:
    def __init__(self, name, age, height="normal"):
    self.name = name
    self.age = age
    self.height = height

tony = Person("tony", 24)
print(f"{tony.name} is {tony.height} height")
```
- we are creating a default value for a variable. so if the user did not give a value for that variable it will use the default. 