# Destructuring Assignment 
#javascript
- - - -
In JS destructuring in unpacking an array or object to assign the values to unpacked variables. 

```js
/* Looks odd but [x,y] is not an actual array it is assigning the variables */
let [x,y] = [20, 30]
console.log(x)
console.log(y)
It looks like an array but because we have let in front of the array we are essentially doing let x and let y 


`let [x,y] = [20, 30, 40, 50, 60]`
You can add additional items but they will be ignored if there are not enough variables
```


```js
  //rest of the items returned as an array
   let [x, y, …rest] = [20, 30, 40, 50]
   console.log(x, y, rest)

  //rest is not a keyword
   let [x, y, …foo] = [20, 30, 40, 50]
   console.log(x, y, foo)
```
Using this syntax will put the rest of the items into one variable and it will be an array. 


```js
//you do not need everything
let me = ["Clint", 29, "clint@digitalcrafts.com", 160]
let [name,age] = me
console.log(name,age)
```
We do not have to use all of the values.


```js
let [name,age,,weight] = me
console.log(name,age,weight)
```
Here we are leaving out the email and we do it like so. 


```js
let me = {name:"Clint", age:29, email:"clint@digitalcrafts.com"}

// A pattern you will see in react ... a LOT
//Grabs the keys and assigns a variable to that named key
const {name,age, email} = me
console.log(name,age,email)

//just like with arrays you do not need to destructure all the parts
const {name} = me
//this is helpful if the object is large and you only need a few parts.
```



```js
const {name:hisName, age, email} = me
console.log(name,age,email)
```
You can use this to have a variable as the value and that variable will hold the name. 













