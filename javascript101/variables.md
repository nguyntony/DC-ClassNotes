## Variables

- there are three ways to declare a variable
- you can declare a variable without assigning a value
``` javascript 
var greeting; 
// this works!
// later you can come back and give the variable a value.
greeting = "hi there!"
```
- do not assign a variable without the syntax 'var', 'let', 'const'
```js
greeeting = "hi there!"
// do not do this please.
```

### what happened to var?
- var isn't really used anymore, use let or const instead!
- var allows the user or code to reassign variables and we do not want that, it may lead to issues...

### what is const?
- const makes it where you cannot change the value of the variable. 
- this is really helpful when you are writing code and you may name variables/functions the same name...which may lead to issues.
- if you define something as a const, you cannot later down in the code try to change the value.
- you cannot declare a const without a value.

### naming conventions 
- js follows camelcase.
- thisIsCamelCase
- the first letter is lowercased and to break up words you should capitalize the word.
    - sidenote: in python we use snake_case (this_is_snake_case)

### declaration
- you can declare multiple variables at one. 
```js
let a, b, c

let a = "red", b = "blue", c = "yellow"

let a, b = "blue", c
```
- you can declare the values if you want and you don't have to declare all of the variables either, some variables can be undefined.