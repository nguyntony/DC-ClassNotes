# Form Tag
#javascript
- - - -
“Submits to the server” stuff in a form tag, after you press the button with the form attribute, will then put it in the URL. 

* `http://localhost:xxxx/folder/?username=cefleet&password=ImAmazing`
From the ? and on it is called the query string

* `console.log(window.location.search) //hard to parse this string`
If you run this code, it will return everything after the ?


```javascript 

let urlParams = new URLSearchParams(window.location.search);

for(key of urlParams.keys()){
	console.log(key, urlParams.get(key))
}
```
You can run this for of loop to be able to grab the keys and the values individually so you are extracting information from the query string.. 


### Action
- - - -
The action attribute in a form will tell the document where to send the information, it will normally be a backend server. 

```html
<!-- action is a url -->
<form id="login" action="login.html">
  ...
</form>
```
For now, we are going to send information to a different file.


```javascript
let loginForm = document.querySelector("#login")
loginForm.addEventListener("submit",(evt)=>{
  evt.preventDefault()
  console.log('I can do something else with the form!')
  console.log(evt.target.elements)//HTMLFormControlCollection


//if it has a name or id you can do this
console.log(evt.target.elements['login'])


//also you can spread it into an array and loop it
let results =[...evt.target.elements]
	.filter(el=>el.name)
	.map(el=>({name:el.name, value:el.value}))


let d = document.createElement("div")
d.append(results[0].name, ":", results[0].value)
document.body.append(d)
console.log(results)
})
```
preventDefault(), running this function will prevent what would happen by default, so here we are using this function so that it won’t add the query string to the end of the url and will not refresh the page. 

Form has a “.elements” 



If we don’t know the values, we can spread the event target and filter then map it. 






























