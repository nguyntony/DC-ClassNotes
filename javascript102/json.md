# JSON
#javascript
- - - -
Javascript object notation: It is away of formatting strings that contains data that can be converted into an array or object for usage in a program. It only contains data!!

```js
let myJSONArray = '["string1", "string2", "string3"]'
let moreJSONArray = '[7, false, true, 42, "more text"]'
```
All string values in json require double quotes. Numbers and booleans do not require double quotes. 



### Syntax
- - - -
```javascript
let myJsonObject = `{
  "name":"Clint",
  "age":39,
  "email":"clint@digitalcrafts.com"
}`
//JSON objects are more like python dictonaries. They require the key to have double quotes.

let arrayOfObjectJSON = `[
  {
      "name":"Clint",
      "age":39,
      "email":"clint@digitalcrafts.com"
  },
  {
      "name":"Anna",
      "age":37,
      "email":"anna@noneya.com"
  },
  {
      "name":"Olivia",
      "age":11,
      "email":"olivia@noneya.com"
  }
]`
//Arrays and objects are allowed to be nested in JSON
```



### Parsing (JSON -> JS)
- - - -
`JSON.parse(argument)` 


```javascript
// myJSONArray, moreJSONArray,myJsonObject,arrayOfObjectJSON from above

let realArray = JSON.parse(myJSONArray)
console.log(realArray) //array of strings
```


```javascript
// array of additional items
console.log(JSON.parse(moreJSONArray)) 
```


```javascript
//real js object
console.log(JSON.parse(myJsonObject))
```


```javascript
//js array of objects
let famArray = JSON.parse(arrayOfObjectJSON)
```



### JS -> JSON
- - - -
```javascript
let myArray = [1,3,4,5]
let jsonArry = JSON.stringify(myArray)
//just a string

let jsonObjString = JSON.stringify({
  name:"Clint",
  age:39,
  email:"clint@digitalcrafts.com"
})
//still just a string
```
When you send data from a server, it doesn’t know how to interpret an object. So you should convert to a string. 



### Errors
- - - -
Functions are other things that JSON cannot turn into a string are ignored. 

























