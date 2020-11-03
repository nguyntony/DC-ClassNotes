## String
```js
"Hi I am a string"
```
```js
`
this
will allow you
to have space
`
```
```js
let a = "hellloooo"
```
- in js if you try to add a number to a string it will not error out, it will forcibly convert the number in a string
``` js
console.log(a + 15)
// output: hellloooo15
```

### formatting
```js
let a = "tony"
let b = 24
let greeting = `${a} you are ${b} years old.
```
- you the back ticks and a dollar sign with curly brackets to basically format

### properties
(sort of like attributes)
- .length = will tell you the length of the string.

- kind of like in python when you access a list using brackets and the index you can access a string in a similar fashion

```js 
greeting[5]
// this will grab the 5th item in the string
```

- charAt() 
    - you pass the letter or item you are looking for and it will return the index, if the item does not exist it will return an empty string.

``` js
let a = "this is the a STRING"
let b = a.toLowercase()

// this will not change the a variable it only returned the return value to the b variable.
```
___

## Number
- these are all numbers:
    - 1
    - 1.5 (in python this is a float)

## properties 
- to.Fixed() 
    - you pass it a number for how many decimal points you want to show.

___

## Booleans
- true 
- false 
- in python it is capitalized but you don't need to do that in js.

```js
let isOn = true
```
- sidenote: this might be a good variable naming for when you want to toggle something in js.
- if you try to add a boolean with a string it will return a string of the boolean but it is still a boolean 

```js
let a = true
console.log(a + "that")
// this will return "truethat"
// but a is still a boolean
```
___

## Undefined and Undeclared
- undefined is different from undeclared. 
- undefined is undefined
- undeclared is not existing

___

## Operators
- let a = 10
    - = is assignment operator
- a += 1
    - += incremeter 
- a -= 1
    - -= decrementer
- %
    - modulo
- a++
    - incrementer by 1
- a--
    - decrementer by 1
- ==  
    - to check if it is equal to
    - let a = 10
    - a == "10"
    - this results in true because it is coercing the string 10 to a number 10 which returns true.
- === 
    - this is the same as above but it will not convert the data type
- != 
    - does not equal to
- !== 
    - strict comparison, will not convert the data type but the one above will. 
- <, >, <=. >=
    - unlike the === or !== there is no strict comparison here for evaluating
    - use Number() to change what you are trying to change the data type.
- && 
    - this works like the 'and' operator in python
    - all of the conditions must be true
- || 
    - this works like 'or' in python
    - as soon as one condition is true, it returns true. 
- you can do something like this
    - (a == 10 || b == 10) && c == 10
    - you need to use the parenthesis here otherwise there will be an error, you are creating two conditions.
- ! 
    - this means not
    - !(true) this means false, the opposite of true is false.

___
## Conditions 
```js
let a = 10
if (a === 10) {
    console.log("a is 10")
}
```
- this is the syntax for writing if statements.
```js 
let a = 10
if (a === 10){
    console.log("a is 10")
} else {
    console.log("a is not 10")
}
```
- else does not have a condition
```js
let a = 10
let b = 20
if (a === 10){
    console.log("a is 10")
} else if (b === 20){
    console.log("b is 20")
} else {
    console.log("a is not 10")
}
```
- fun fact: else if isn't necessarily elif in python but it does allow us to achieve the same goal. 
- you can do nesting if statements in js.

## ternary way 
```js
let a = 10
a === 10 ? "yes" : "no"
```
- condition/expression ? value if true : valure if false
- you can assign this to a variable
``` js 
let result = a === 10 ? "yes" : "guess again"

// this is the same as ...

let a = 10
if (a === 10){
    let result = "yes"
} else {
    let result = "guess again"
}
```
- if you are only getting one value returned, the ternary way is the more correct way to do this situation.

## if statement one-liner
```js
let a = 20
if (a > 5) console.log("Yes it's more than 5")
```

## switches
```js
let a = 10
switch (a) {
    case (value):
        // code
        break;
    case (value):
        // code
        break;
    case (value):
        //code
        break;
    default:
        //code
}
```
- this "switch (a)", the a is a value not a condition
- condition is good if you are trying to see what the value is and have it do x, y, z.
- you need to use break 
- for the default you don't have to use break.

```js 
let number = 12 //random input from user
let output;
switch(true){ //doing this compares to see if each expression is true
    case (number < 3):
        output = 'low'
        break;
    case (number < 7):
        output = 'med'
        break;
    case (number < 14):
        output = 'high'
        break;
    default:
        output = 'very high'
}
```
- so here, we can replace the switch (variable) that we are checking with each expression.