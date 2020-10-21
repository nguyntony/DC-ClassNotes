## Dictionary

- similar to list but uses a key value pair to access the dictionary.

``` python
sibling = {
    "name": "Michelle"
    "age": 18
    "fav_color": "mint"
}
```
- the keys here are: name, age and fav_color.
- keys can be a number or a string. 
- it has to be hashable. 

### Accessing dictionaries

``` python
sibling[name]
print(sibling[name])

# Michelle
```

### What can the values be?
- the values are currently: Michelle, 18 and mint. 
- values can include a list and boolean. 

```python
sibling = {
    "name": "Michelle"
    "age": 18
    "fav_color": "mint"
    "fav_foods": ["cheese", "steak"]
}
``` 

- to access the list:
```python
sibling["fav_foods"][0]
```

### How to search for items
```python
search = "name"
for search in sibling:
    
