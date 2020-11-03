## while loop
```js

let i = 1;

while (i < 10){
    console.log(i)
    i++
}
```

- very similar to python while loop.

``` js
num = 10
for (let i = 0; i < num; i++){
    console.log(i)
}
```
- you can change the i++ to i+=2
- this is a standard way for using a for loop.

``` js
let i = 1
for (; i < 20; i++){
    console.log(i)
}
```
- here we stated the initial/starting value outside of the for statement.
- you can also leave the incrementer or decrementor out of the for statement and put it inside of the code block, 
- you could also leave out the condition but here you are writing an infinite loop.

## break out of loops
- a one-liner break statement 
- if (i > 5) break;
    - if i is greater then 5 then break.
- break will take me out of the loop

## continue
- continue you continue to the next iteration of the loop
- continue will ignore the present/current iteration of what you are trying to do

``` js
for(let i = 0;i<20;i++){
    if(!(i % 2)) continue;
    console.log(i)

// this will print the odd numbers. 

}
```