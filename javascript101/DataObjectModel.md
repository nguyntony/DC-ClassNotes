# Data Object Model (DOM)
#javascript

### Preface
- - - -
*Local web server*: some parts of JS need a server to operate correctly. A local server is web server that runs on your local computer in order to host these websites for testing and development.

*Port*: in web terms, port is a numbered address that allows data traffic to flow. Ports must be opened and ready to receive data if it can be used

*URL*: URL is directed using a domain name service (DNS), your computer has a domain server and it will tell you where this url should go. It tells you where to go by returning an IP address. 

*Localhost*: localhost is the local address for a development computer. It only points to the computer you are currently using. It is also written 127. 0.0.1 (this number will always go to your local machine)

*TLDR*: if you type in localhost in a browser, it will not go out into the worldwide web ever, it is on your local machine that is hosting information. http://127.0.0.1


### Setting up a local host
- - - -
1. In the terminal, go the folder that you wish to be in
2. In the terminal, type: `python3 -m http.server 5000`
3. Now you can go into the your browser and type in: `localhost:5000`

*General rule*: **DO NOT** host a directory that may contain anything personal or confidential in that directory. 

The 5000 that we pass can be a different number but don’t use a number <3500 or >9000.

After you have set up this local host you will hit CTRL-C in the terminal and it will exit the localhost. 




# What is DOM?
- - - -
It is how JS view the html page. Every element is part of an object that is a tree type structure and has parents and children. 


### Accessing the DOM
- - - -
**Grabbing elements from HTML**
```javascript
let paragraphs = document.getElementsByTagName("p")
console.log(paragraphs)
```

This will return an HTML collection in the browser console.
HTML is a list of elements that is returned from the .getElementsTagName/ClassName, it cannot be looped over using the forEach(). 


### Access an HTML Collection
- - - -
If you wanted to access the list you can use [index] to grab a specific element in the list.
* `console.log(paragraphs[1])`
If you use this method, this will log what it appears to be in the HTML doc. So it will return that specific p tag from the HTML

* `console.dir(paragraphs[1])`
If you use this method, this will log the specific element or object and return what this element/object has. 

**What does it return?**
- - - -
In this “paragraphs” example, there are multiple p tags in HTML but if you were to getElementsByClassName, (and if there were a single item) it will still return an HTML collection. If you are trying to access a tag or class name that does not exist, it will return an HTML collection but it will be empty. Apparently you can still iterate this empty collection. (It will just iterate it zero times)

If you select an id that does not exist, it will return an HTML collection that is null

*querySelector*: will only return one item and it should be the first item that it finds. if you are trying to select an item that does not exist then it will return null. You can pass it html tags, “#id”, “.class” You wouldn’t really querySelector when you are trying to select a class that has multiple instances, you are using this to select one item. 

*querySelectorAll*: this will return a Node List (eg. .subclass (class=“subclass”)) and unlike the HTML collection you can use the .forEach() on the Node List.


### Selecting elements in DOM
- - - -
- document.getElementsByTagName()
- document.getElementsByClassName()
- document.getElementById()
- document.querySelector()
- document.querySelectorAll()
- setAttribute()

You can pass the syntax of CSS selectors (eg. “#id”, “.class”)


### How to create a new element using DOM
- - - -
**.createElement()**
```javascript
let content = document.createElement("div")
let ul = document.createElement("ul")
```
If you console.log these variables, you won’t be able to edit them in the browser console. 
When you create something (in this manner), you created it but it isn’t attached anywhere. After you created it, you have to add it.


**.append()**
```javascript
let main = document.querySelector("main")
main.append(content)
```
This is how you append the newly created item to the document, there is a main tag  in the HTML doc and you will append this “content” to the end of the main tag. 


**unordered lists**
```javascript
for (let i = 0; i < 6; i++){
	let li = document.createElement("li")
	li.append(`this is item#: ${i}`)
	ul.append(li)
```
You will create six li items by using this for loop. 
We are appending the li items to the ul variable which is the ul tag we declared above.
`let ul = document.createElement("ul")`


**content creation**
```javascript
let p = document.createElement("p")
p.append("This is going to be a p tag")
```
You are creating a p element and appending a string to it but this will not appear on the html document because you need to append the element to the document.
So you can append this to the body tag or maybe another tag that you have like a section. 


```javascript
let section = document.querySelector("section")
section.append(p)
```


**.innerText**
```javascript
let header = document.querySelector("h1")
header.innerText = "I want to change my h1 text."
```
innerText will always to text, so if you try to create a div tag inside of the argument you are passing, it will not work. 


**.innerHTML**
```javascript
let para = document.createElement("p")
para.innerHTML = "this is add text"
```
This is another way to do what .innerText() but it will allow you to write html tags inside, so if you write a div tag it will work. 
This is the least preferred way to create content. 


### How to add/change attributes to elements 
- - - -
```javascript
let main = document.querySelector("main")
main.id = "main-content"
```
This will set the id of the main tag to “main-content”

```javascript
let link = document.createElement("a")
a.innerText = "this text will be a hyperlink"
a.href = "google.com"
```
This will create an a tag with a href of google.com and the hyperlink text will show the .innerText

```javascript
let div = document.createElement("div")
div.className = "classname"
```

This is an alternative way of setting and changing attributes with DOM, the other way is setAttribute().


# Modifying Styles in DOM

**style attribute**
```javascript
let header = document.querySelector("h1")
header.style = "border-bottom: 1px solid black; text-align: center; color: red;"
```
This is similar to setting attributes, what we did above, there is a style attribute that we can set and modify on specific elements. 

```javascript
let paras = document.querySelectorAll(".p-child")
let styleString = "color: blue;"

paras.forEach(p, idx){
	p.style = styleString
}
```
paras will select all classes with “.p-child” and then we set the style string to a variable styleString and we will loop through paras and for each one we will set a style attribute. You can loop through this because it is a Node List and you can loop through it, if it was an HTML collection you wouldn’t be able to use the .forEach()


```javascript
header.style = "green"
```
**NOTE**: if you were to try to edit the style attribute for an element by modifying it, it will clear out the whole style attribute. 


```javascript
header.style.color = "green"
header.style.borderBottom = 4px solid black
```
This will not get rid of all of the styles and only change the color. If you try to access a style that is hyphened you can use camelcase to then edit it

* border-bottom = borderBottom
* font-size = fontSize
* font-family = fontFamily




# TLDR - Create DOM elements
- - - -
1. Declare variables 
2. .createElement()
3. .createTextNode()
4. .append() / .appendChild()

- - - -
Start by figuring out what elements you want to work with and if you want to create a new element make sure you append it to the write place and make sure you are creating a text node or some string. 




# Modifying Classes 
- - - -
Something cool that we can do with the DOM is that in our css file we can have classes that have some sort of styling and these classes that we created in css doesn’t have to be applied anywhere on the html doc….yet. Using the DOM we can add the class to the html elements which will then change the styling or whatever we want. 


### classList
**.add**
```javascript
let footer = document.querySelector("footer");
footer.classList.add("classname")
```
Use the html element variable .classList and .add and you pass the class name to the add() and this will always be the name of the class not a css selector (eg. Don’t do this .add(“.classname”)


**.remove**
```javascript
footer.classList.remove("classname")
```
This will remove a class and apparently you can remove a class that isn’t even attached to the element, it won’t error.


**.toggle**
```javascript
let myInterval = setInterval(function(){
	myButton.classList.toggle("hidden")
}, 500)
```
This will toggle a hidden class on the button and using the setInterval class allows us to pass the second argument, 500 which is every 5 seconds. 

What is actually happening behind the scenes is that it is adding and removing the classes on and off, so an html element does not need to have that class per say in order to toggle. 























































