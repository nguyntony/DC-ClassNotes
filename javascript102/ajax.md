# Ajax 
#javascript
- - - -
History lesson: asynchronous javascript and xml 
This allows you to try to get something information and still have the program run and eventually when the information comes back, your program knows what to do with it. 
Asynchronous basically means multitasking and you’re able to still run your program without stopping because you can request for information without needing it to stop the program. 

### How to get started
- - - -
1. Initialize a request `const request = new XMLHttpRequest()`

2. The request has an event “on ready state change” 
There are four phases and each phase is a number that describes the process or state that it is in. 
```javascript
request.onreadystatechange = (evt) => {
	let req = evt.target;
	if(req.readyState !== 4) return;
	if(req.status === 200 || req.status == 304) console.log(req.response) // this is all on one line
}
```
Req is the same thing as the request object.

3. You have to open the request otherwise you can’t do anything with it. You open it with the open method/function and the first argument is GET (for now) and the second argument is the file path
```javascript
request.open("GET", './folder/filename.txt')
```

4. Now that we have opened it, we need to do something with it. So using this command will allow the process go to phase 4 which means the request is finished and ready.  `request.send()` 

5. This will grab information from the file that you gave as an argument in step 3. And this information will be sent to the browser in which you linked your script file in the html. 

6. If there is an error that occurs then it will say “404” not found in the browser under the Network tab. This is saying that the data you are looking for does not exist. 


### Turn it into a module to reuse
- - - -
We can turn what we did above into a function and let it live in a file and we can import it. 

1. Create a file named “ajax.js” (can be named something else

2. Helper file
```javascript
const ajax = (url, callback, method="GET") => {
	const request = new XMLHttpRequest();
	request.addEventListener("readystatechange", (evt) => {
		let req = evt.target;
		if (req.readyState !== 4) return;
		if (req.status === 200 || req.status === 304) return callback(req.response) //this is all on one line
		callback(null, req.status)
	})
	request.open(method, url)
	request.send()
}

export default ajax;
```

3. In a different file
```javascript
import ajax from "./folder/ajax.js"


ajax("test.txt", (resp)=>{
	let div = document.createElement("div")
	document.body.append(div)
	div.append(resp)
})

// you can also create a callback function outside of the parameter if it is easier to read/understand

const callback = (resp) => {
	let ul = document.createElement("ul")
	let li = documnet.createElement("li")
	li.append(resp)
	ul.append(li)
}
ajax("test2.txt", callback)
```
First parameter: the url that the user supplies
Second parameter: the callback function that describes what the user wants to do

**Note:** for our callback function, we called it resp but that is an argument that we supply which is a variable that holds the information in that file path, we can call it something else if we wanted to. 

**IMPORTANT** this is asynchronous and the server will send it whenever the file is ready so if you fire off multiple requests you cannot control which order or which one will come first. 





