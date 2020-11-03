```js
function funcName(){
    //code
}
```

```js
function funcName(){
    return "I have returned"
}
```
- this returns a string
- but this won't console.log anything because it is not set to do so

```js
let result = funcName() + ' and I am adding this."
```
- this will concatenate the strings.

```js 
function funcName(name){
    console.log(`I think your name is ${name}.`)
}
```
- sidenote: you can give the function more than one parameter when it only accepts one argument, this is will not error out.




## anonymous function
``` js
const myFunc = function(someArg){
    console.log("I'm anonymous", someArg)
}
```
- anon functions cannot be called for however, defining a function through the normal way you can use the function before it is created, apparently.

- when js is trying to run code, it will go through once and look at functions first and then go back through and execute the code which is why you can call functions before they are defined in the order that the code appears.
- for anon functions you are defining them through a variable which then does not fulfill that condition bc when js goes through to try to run the code it will ignore the variable first. 


- you can give anonymous functions as an argument to another function. 
```js
function hasArgumentFunction(argFunction){
    console.log('I have a function as an arg')
    argFunction()
}

hasArgumentFunction(function(){
    console.log('Ok this is ok')
})
```
## advantage of anon func

```js

function foo(bar){
    bar()
}

foo(function(){
    console.log("foo, bar")
})
```
- the function that you are passing in foo is in the parameter bar which is why when you created function foo with bar() it is ran as a function.

- it is expecting a function so you have to pass a function

- you can create an anon function as a parameter in another function