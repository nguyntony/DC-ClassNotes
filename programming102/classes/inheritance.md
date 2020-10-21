## Inheritance

``` python
class Mob:
    def __init__(self, name, health = 10, atk_power = 2):
    self.name = name
    self.health = health

    def get_hit(self, atk_power):
        self.health = self.health - atk_power
        print(f"I, {self.name}, have taken {atk_power} dmg.")

    def attack(self, enemy):
        enemy.get_hit(self.atk_power)

class Hero(Mob):
    
    def __init__(self):
        self.name = "tony"
        self.health = 100
        self.atk_power = 10

    def yell(self):
        print(f"I am yelling my name, {self.name}")
    
    def get_hit():
        print("I'm getting hit!")
        super().get_hit(atk_power)

hero = Hero()
hero.yell()
print(hero.atk_power)
villain = Mob("Tyler")
hero.attack(villain)
print(villain.health)
```

- you can create another class and pass a different class as an argument and it will use that class as a blueprint
    - it will inherit the information defined there.
    - so here, we created Hero and it will inherit from Mob.

- any information you have in the new class will not accessible to the other class. 

- you can create a new __init__ in the sub/child class and override information from the parent. 
    - now the hero class will not accept any arguments and have default information unlike the mob class. 

- you can also overide the class method in the child class 
    - so we can ovveride the get_hit function from the parent mob class. 

- super 
    - super().get_hit(power)
    - super() can be used so that the child can still get information from the parent class
    - this way you can add information but not override information that may be valuable.
    - you wouldn't want to override code that you plan on using it again, this will keep your code dry. 
    