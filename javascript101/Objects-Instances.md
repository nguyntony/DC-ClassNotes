# Objects 
#javascript
Everything is an object in JS. 
How do we know that?

```javascript
console.log(typeof "yes" )
console.log(typeof new String("yes"))

let myString = "yes"
let anotherString = new String("yes")

console.log(myString, myString.length)
console.log(anotherString, anotherString.length)
```
typeof will tell you the type of the value or whatever. these two have the same properties and behave similarly. 

* anotherString is an instance of a string but it is also an instance of an object.
` new String (“yes”) instanceof Object ` 	output: true
` new String (“yes”) instanceof String `	output: true
` new String (“yes”) instanceof Array `	output: false
instanceof will tell us whether what it is we are checking will be an instance of an Object, String or Array.
There isn’t really a “class” in JS, unlike in python.

```javascript
function Animal() {}
let cat = Animal()
```
_What is cat?_	Right now, with this code, cat is undefined but if you write it using the new operator
```javascript
function Animal() {}
let cat = new Animal()
```
Now cat will be an instance of Animal()

### Instances
```javascript
function Animal(name, type, noise) {
	this.name = name;
	this.type = type;
	this.noise = noise
	this.nameNoise = function(){
		console.log(this.name + "says " + this.noise)
}

let cat = new Animal("shadow", "cat", "meow")
```
* Cat is now an instance of Animal and it will have those properties and you can access it like so
`cat.name`	output: “shadow”

* You can also have a function inside of this instance and then call it. It’s called sort of like a method.
`cat.nameNoise()`	output: “shadow says meow”

* You can also loop through this instance and name all of the “keys”
```javascript
for (key in cat){
	console.log(key)
}
```

* This is object oriented programming. This sort of code you will not see that often in the wild but it is out there. 


### JS is a prototypical language
It is not a norm to have a function inside of the Object or “class”
Above, we wrote the nameNoise inside of the Object or “class”, that is not the norm, you would give it to the prototype by doing this
```javascript
Animal.prototype.nameNoise = function(){
	console.log(this.name + "says " + this.noise)
```
So now cat has this function that it can do but it is not located in the Object or “class”

If you wanted to loop through the properties of cat you can use a for loop but it is important to note that you need to do it like this, otherwise the nameNoise will also appear. 
```javascript
for(property in cat){
	if(!cat.hasOwnProperty(property)) continue;
	console.log(property, cat[property])
```
If you did not include this if statement then it will show four properties but there is only four which should be name, type and noise.
nameNoise should not appear and it won’t if you loop through it like above. 


### Prototype
What is prototype? 	_Prototype is an instance of the Object_
On MDN, if you see Array.prototype.reverse() when you see this you can call it on the instance of that Object.
```javascript
let newArray = [1,2,3]
newArray.reverse()
```

However, there are ones listed where prototype is not there, in that case you would write it like this
`Array.isArray(newArray)`
Here you would have to the Object itself then pass the instance as an argument in that method





