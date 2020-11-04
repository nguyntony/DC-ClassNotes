# Objects (Javascript) 
#javascript
The way that we are talking about to objects right now is about how it is a data type

* this is how you declare an object
```javascript
let myObj = {}
```

```js
let newObj = {
name: "tony",
age: 24,
asian: true
}
```

## How do we access this object
```js
newObj["name"]
```

* this will return “Tony”

### You can also access keys by using the dot notation
```js
newObj.name
```

### What if we want to edit the values of the keys?
```js
let newObj = {
name: "tony",
age: 24,
asian: true
}

newObj.name = "Tony Nguyen"
```

* this will change the name key to be “Tony Nguyen” now.


### You can also update the values like this
```js
newObj.name += " N."
```
This will append that string to the end of the name value.


### You can also use this method to create more key value pairs
```js
newObj.gender = "male"
```

### If you wanted to delete something
```js
delete newObj.gender
```

This will delete the gender key and it will no longer be in the newObj.




## How to loop through an object
```javascript
for(attribute in newObj){
	console.log(attribute, newObj[attribute])
```
So we are creating a temporary variable called attribute and we are passing the keys to this variable which is why when we try to console.log this, we also supplied it the variable in the [] because it will hold the key name. 





```javascript
for(attribute in newObj){
	if(!newObj.hasOwnProperty(attribute)) continue;
	console.log(attribute, newObj[attribute])
```
This is apparently the more correct or modern way to loop through an object. There are sometimes in Javascript that objects may have extra attributes that comes from inheriting or by simple design of javascript and adding this if statement will leave those extra attributes/properties out. 

Is it possible to iterate over unexpected instances? **Yes**, with that being said this if statement will allow it to not do that.




## Array of Objects
Let’s say that we want to create an array of people. You will create an array but each item in the array will be an object, like so.
```javascript
let people = [
	{
		name: "tony",
		age: 24
	},
	{
		name: "tyler",
		age: 25
	},
	{
		name: "michelle",
		age: 19
	}
]
```
The way to access this array is:
	* You first need to grab the object index, so if we want to access Tony you need to do:
	`people[0]`
	You need to do this people Tony is at the index of 0

	* Now if you wanted to access the name you would do:
	`people[0].name`


### How to loop through an array of objects
```javascript
people.forEach(function(person){
	console.log(person.name + " is " + person.age " years old.")
})
```


### How to sort an array of objects by the key value

You need to use the .sort method and also a callback function, if it returns -1 or 1 it switches the order of the  objects in the array.
```javascript
people.sort(function(a, b){
	return a.age - b.age
})
```
This is a pretty standard way that you can sort the objects in array  by a key. This will order the objects from the youngest age to the oldest. 

If you wanted to give the oldest to the youngest you can call the .reverse()  after the .sort()
```javascript
people.sort(function(a, b){
	return a.age - b.age
}).reverse()
```


