# Spread Operator 
#javascript
- - - -
The spread operator will 


```javascript
let array1 = [1,2,3]
console.log(array1)

let array2  = [...array1,4,5]
console.log(array2)
```
If you console.log array1 it will return an array but if you console.log array2, it returns the items in the array as separate numbers and it will not appear in an array and we have also added 4 and 5 but because we also wrapped it around [] it returns the whole thing in an array.


```javascript
// syntax
{...iteratableObject, key1:value1, key2:value2}

let me = {firstName:"Clint",lastName:"Fleetwood", email:"clint@digitalcrafts.com"}

let newPerson = {age:39, ...me}
console.log(newPerson)
```


```javascript
let updated = family.map(member => ({...member, surName: "Nguyen"}))
```
This allow you to copy the source array but a new attribute surName to it and then you still have source array untouched but a new array that you can manipulate. 


```javascript
//update a single item from the list as filtered
let oliviaMarried = {
  name:"Olivia",
  surname:"Musk",
  age:24
}

//cool but it's at the end
let updated = [...family.filter(p=>p.name != 'Olivia'), oliviaMarried]

//using sort to keep the same order
let filtered = family.filter(p=>p.name != 'Olivia')
let updated = [...filtered, oliviaMarried]
.sort((a,b)=>b.age - a.age)
/* The Above Pattern you will see again...Take Time to learn it*/
```


It is important to note that using sort will affect the original array.




