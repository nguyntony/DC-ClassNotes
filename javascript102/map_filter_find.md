# Array Map, Filter, Find
#javascript #ES6
- - - -
Functions to be used with arrays. 



# Map
- - - -
Use this function when you want to return a new array, you do not want to change the original array whatsoever.

```javascript
let letters = ["a","b","c","d"]
let letterPlus = letters.map(letter => letter + letter)
console.log(letters)
console.log(letterPlus)
```
The .map will look very similar to .forEach()

* **What does .map do that .forEach() doesn’t do?**
It creates a new array that is the exact same length as your starting array. It takes the return value of each callback and places it in a new array where the source element is. It loops through the array just like forEach but it has this added functionality. And this will not have an impact to the original source

The whole point of map is to create a new array 


**Another example**
```javascript
let letterObj = letters.map((letter,idx) => {
  return {
      name:letter,
      index:idx,
      letterIdx : letter+idx
  }
})

console.log(letterObj)
```
In this example we want to create a new array of objects which is why the return statement looks like so. We are mapping through the original array (letters) and we are creating a new array that will return the name of the letters, index and letter + index all in an object. 


**Common usage**
```js
let family = [
  {
      name:"clint",
      age:38
  },
  {
      name:"Anna",
      age:37
  },
  {
      name:"Olivia",
      age:11
  },
  {
      name:"Alle",
      age:9
  },
  {
      name:"Mark",
      age:9
  }
]

//returns just names
let justNames = family.map(member => member.name)
})
```
Here you are just grabbing the name attribute from each object in the array. 

You should not be modifying the original array by using map. It can be done but you shouldn’t. 


```js
let updated = family.map((member)=>{
  let newMember = {}
  for(key in member){
      newMember[key] = member[key]
  }
  newMember.surName = 'Fleetwood'
  return newMember
})
console.log(updated)
console.log(family)//no change
```
In this example, what is important to note is that you wanted to add something to the original array but like we said above, you shouldn’t use map to change the original array, but you can use map to return a new array and add a new attribute to each object in the array
* let updated is going to be the new variable that we are going to call our new array
* let newMember = {} is going to create a new object for each source element (which in this case is also an object, the source elements from family is an object)
* we’re using a for in loop to access the keys in the member of family and we are assigning that to the newMember
* and lastly we are appending a new attribute with newMember.surname and we assign it a value and it returns newMember because it will return each object to that array which is updated. 





# Filter
- - - -
Filter always returns an array and for each item if the function returns true, that item is added to the new array.  If all of the items is false, it’ll still return an empty array. And the filter array will never be larger in length than the source array. 

```javascript
let numbers = [5,3,-10,3,-21,78,-54,-1,8]
let positive = numbers.filter(num=>num > 0)
console.log(positive)
```

Filter is not designed to modify the item as it is added. It is designed to simply filter out items from the array.

The num > 0 is an expression/condition that will return a boolean and filter is able to read the boolean and only append “true” items, whatever passes that expression. 


**Common usage**
```javascript
let ships = [
  {
      type:"freighter",
      name:"falcon"
  },
  {
      type:"fighter",
      name:"xwing"
  },
  {
      type:"bomber",
      name:"ywing"
  },
  {
      type:"fighter",
      name:"tie-fighter"
  }
]

let fighters = ships.filter(ship=>ship.type == "fighter")
```
We are filtering the ships array and we only want data that the type is fighter. 
Note that this is using the implicit return if you wanted to add the { after the => you will need to include “return” 



**Using filter and map together**
```javascript
let figherNames = ships.filter(ship=>ship.type == "fighter").map(ship=>ship.name)


// may also look like this in the wild
let figherNames = ships
.filter(ship=>ship.type == "fighter")
.map(ship=>ship.name)
```
Here you can chain the two together so instead of creating a filter array and then creating new map array with another variable you can change the two together if you know that you specifically want something. 


Where that expression is in the filter you can actually filter out objects that do not have the same property. So if the source array has objects that have attributes but not all objects have that attributes you can do 
```javascript
let filterArray = sourceArr.filter(item=>item.attribute)
```




# Find 
- - - -
Find will always return 1 item, once it finds that item (the first item) it will stop there. If it cannot find the item it will return undefined. 

```javascript
let numbers = [1,2,3,4,5,6,7,8]
let more = numbers.find(num=>num > 5)
```
Find doesn’t sort so if you have an unsorted list and the first item so happens to meet the criteria of your expression or condition, it will return that item.





















