## Function Delcaration
1. standard way
```js
function oneWay(){
    console.log("This is one way to create a function.")
}

oneWay()
```

2. anonymous function 
```js 
const anonFunc = function(){
    console.log("This is an anonymous function.")
}

anonFunc()
```

### Key takeaways
- when declaring an anonymous function you can NOT call on it before declaration.

- the function is anonymous, note how it has no name, there is no way to really call the function except that we assigned it a point of reference through a variable assignment.

- when creating an anonymous function it is best to use const because it will help reduce redundancies and errors that may occur.
___
### An advantage of anonymous functions
- you can create an anonymous function when passing it as an argument for another function. 

```js
function mainFunc(anon, num){
    let i = 0;
    for (;i <= num; i++){
        console.log(i)
    }

    anon()
}
```
- mainFunc takes two arguments it has an anon and num parameter.

- the best way I understood this is using function in python

```python
def greeting(name):
    print(f"I think this is your {name}.")
```

- we can pass any value in this greeting function
- when we are passing the value here, the function understands that the value will be temporarily assigned to name so that it can perform what the function needs to do.

```python
greeting("Tony")
```
- here, "Tony" which is a string is being referred to as name which is then later used in the print statement.

___
- Now back to the js anon function
```js 
function mainFunc(anon, num){
    let i = 0;
    for (;i <= num; i++){
        console.log(i)
    }

    anon()
}


mainFunc(function(){
    console.log("this is the anonymous function")
}, 5)

```
- we are passing this anonymous function:
```js
function(){
    console.log("this is the anonymous function")
}
```
- in place of the anon, which is why when we call it in the mainFunc it is used as a function because we also added "()"

- anon does not need to be previously defined because it is used as a reference for the function just like in greeting
- name is not defined at any point, only when we call the function and pass it a value then name has some sort of information. 

___

- now in the mainFunc() we also did "anon()" because we are expecting a function.
- this is very similar to when we are creating functions that deal with numbers. 
- for instance:

```python
def divide(num1, num2):
    total = num2 / num1
    print(total)
```
- in this function we are using division and this only works on numbers.
- if we were to pass it a string, it would error
- there are ways to handle this error but that won't be covered here. 

___

- this is very similar if not the same thing that we are doing here:

```js 
function mainFunc(anon, num){
    let i = 0;
    for (;i <= num; i++){
        console.log(i)
    }

    anon()
}
```
- we are passing a parameter and we have some expectations of what we want it do or what the function is designed to do
- similar how the divide() is meant to divide numbers, you are expecting numbers.

- here this function is expecting to call an anonymous function, which is why there is an "anon()" within the function. 

____

### Another way to see it
```js 
function anotherFunc(anon, name){
    console.log(`I think your name is ${name}.`);

    anon()
}

const anonFuncAssignedToVariable = function() {
    console.log("I am the mysterious anonymous function.")
}

anotherFunc(anonFuncAssignedToVariable, "Viet")
```

- here we assigned the anonymous function is assigned to a variable and later we pass that function to anotherFunc. 
- what we did above, shows that we can cut out the middle man on assigning it to a variable. 