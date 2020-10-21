## Class methods

```python
class Mob:
    def __init__(self, name, health = 10):
    self.name = name
    self.health = health

    def get_hit(self, power):
        self.health = self.health - power
        print(f"I, {self.name}, have taken {power} dmg.")

hero = Mob("Sir Blue", 30)

hero.get_hit(6)
# Output: I, Sir Blue, have taken 6 dmg.
print(hero.health)
# Output: 24
```

- when creating a func inside of a class you need to give self as the first parameter. 
- self.health is only affecting the instance of that object. so Sir Blue lost health but if we create a new character then it will be unaffected on sir blue


```python
class Mob:
    def __init__(self, name, health = 10):
    self.name = name
    self.health = health

    def get_hit(self, power):
        self.health = self.health - power
        print(f"I, {self.name}, have taken {power} dmg.")

    def attack(self, enemy):
        enemy.get_hit(self.power)


hero = Mob("Sir Blue", 30)

hero.get_hit(6)
# Output: I, Sir Blue, have taken 6 dmg.
print(hero.health)
# Output: 24
badguy = Mob("Villian", 100)
print(badguy.health)
# Output = 100
```

### Return value in class methods
- you can return a value in a class method. 

- you can create a class method which passes another class object. 


