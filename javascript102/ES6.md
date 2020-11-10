# ES6 
#javascript #ES6
- - - -



### Template Strings 
- - - -
Similar to python where you use the f-string format to write a string and call variables inside of the string you can do that in JS as well.

* You use back ticks to be able to format string: console.log(`this is a string ${b}`)

In python we call them f-string but in JS, they’re called template strings and you can use ternary operators inside of them. 

The big idea is that if you want to include something inside of the template string, whatever you are calling inside of it, it needs to return something. So you could have a function that returns a string and you can do ${func()}



# Arrow Functions
- - - -
In some ways arrow functions are anonymous functions you need to assign it to a variable or use it in someway where you can access what it is trying to do so that you can reference it and actually use it. 

# What does it look like
```js
const myArrowFunc = (foo) => {
	console.log(foo)
}

myArrowFunc("hi there!")


// Another way 
const returnStuff = (arg)=>{
  return 'stuff'+arg
}
console.log(returnStuff('something'))
```
The returnStuff function returns something, so this has the same usage as a regular function. 

- - - -
# Things you can do with an arrow function
* If you have a single argument you do not have to wrap it around parentheses . 
```js
const myArrowFunc = foo => {
	console.log(foo)
}
```


* Arrow functions allows you to have an implicit return
```js
const returnStuff = arg => 'stuff' + arg
```
So if you write the function like this (without the curly bracket and the return keyword) it will implicitly return “stuff” + whatever value you gave it

```js
const returnStuff = arg => console.log('stuff' + arg)
```
If you include the console.log, it will print your statement but also return undefined, so you do not need to include it. 

You can have an arrow function return something and then use that function along with another function to join the returns that each function would do. 


- - - -
* You can pass a function as an argument and that is known as callback function
```js
const doSomething = function(callback){
  console.log('I did something')
  callback()
}

doSomething(()=>{
  console.log('The function is finished and now it is my turn')
})

//condensed callback
let myArr = ['a','b','c','d']
myArr.forEach((letter,idx)=>console.log(letter, idx))
```
You see that the doSomething is expecting a function (similarly to anon functions) and you pass the arrow function in the doSomething function

In the last example, we are condensing what we have to write for a for loop what will pass through an array. 






































