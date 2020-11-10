# UI API
#javascript  #html #inputform
- - - -
Forms are naturally inline elements but you can change the display to block elements if you want. 



```html
<input  />
```
There are several attributes that you can do
* id=“username”
* class=“special”
* name=“user-name”
* placeholder=“Username
* value=“whatever value”

The name attribute usually has the same value as id. And input forms need a name. 

Placeholder is not the same thing as value, you can have a default value with the value attribute and if you hit submit, it will actually use that default value you set. 

```html
<input 
  id="username" 
  class="special" 
  name="user-name"
  placeholder="Username"
>
```

### Type
- - - -
* type=“password”
If you were to type in the field with that it will hide the characters, this does not put encryption or anything. 
* type=“radio”
* type=“checkbox”
* type=“text” 
If you do not declare the type of input, the default it text. 
* type=“email”

### Label
- - - -
Each input box will usually have a label, this will appear before the input box. 
```html
<label for="username">User Name</label>
<input 
  id="username" 
  name="user-name"
/>
<!-- clicking on the label is the same as clicking on the element if the for is a valid id -->
<label> User Name
  <input id="username" name="user-name">
<label>
<!-- this is another way to assign a label to an element-->
```
You use the for attribute in the label tag and you pass it the same id as the element you wish and now when you click on the label it will put the cursor in the input box. 


**instead of using for you can next the input in the label tag**
```html
<label for="username">User Name</label>
<input 
  id="username" 
  name="user-name"
/>
<!-- clicking on the label is the same as clicking on the element if the for is a valid id -->
<label> User Name
  <input id="username" name="user-name">
<label>
<!-- this is another way to assign a label to an element-->
```
This may make it difficult to grab the input tag and style it. 




### Checkbox
- - - -
Checkbox elements are meant to be toggled and you can choose more than one. 


```html
<input type="checkbox" id="agree" name="agree">
<label for="agree">Agree To terms?</label>
```
You can use the label for so that you can just click the label vs the little box. 
When looking at the checkbox information, whatever the name is, it’ll say (in this case) “agree = on” if the checkbox is not checked then it will not even have that information. 

You change that “on” by including a value in the input so if the value is “I agree” it’ll say the name then the value if you checked it. 
```html
<label> I like dogs! <input type=“checkbox” name=“thoughts-on-dogs” value=“dogsFTW”></label>
```


**checked**
```html
<input checked type=“checkbox” id=“agree” name=“agree”>
<label for=“agree”>Agree To terms?</label>
```
Checked here means true and absence of value means false. 


```html
<div class=“checkbox-group”>
  <label> Cars 
      <input value=“cars” name=“transport” type=“checkbox”>
  </label>
  <label> Trains 
      <input value=“trains”  name=“transport” type=“checkbox”>
  </label>
  <label> Planes 
      <input value=“planes” name=“transport” type=“checkbox”>
  </label>
</div>
```
These input have the same name. 


### Radio
- - - -
This is not like checkboxes, you cannot toggle this on and off without js. 

```html
<label for="myRadio">Radio</label>
<input id="myRadio" type="radio">
```


```html
<div class="radio">
  <label for="cars">Cars
      <input id="cars" name="transport" value="cars" type="radio">
  </label>
  <label for="trains">Trains
      <input id="trains" name="transport" value="trains" type="radio">
  </label>
  <label for="planes">Planes
      <input id="planes" name="transport" value="planes" type="radio">
  </label>
</div>
```
This is the same format as the one above but it is type radio. Since these have the same names you are able to select another radio button within that name group. 



### Select Element
- - - -
This is a dropdown menu/select

```html
<label for="favorite-food">Favorite Food</label>
<select name="favorite-food" id="favorite-food"></select>
```


**option**
```html
<label for="favorite-food">Favorite Food</label>
<select name="favorite-food" id="favorite-food">
  <option value="pizza">Pizza (Ninja Turtles)</option>
  <option value="mushrooms">Shrooms (Mario)</option>
  <option value="doughnut"> Doughnuts (Homer)</option>
</select>
```
The value is what is being sent to the server. Not what is in the text field. If you don’t have a value set it will send what is in the text field. 

If you wanted, you can set a default option by adding selected in the tag. But in react you need to have the value set in the select tag. 

An empty string set to value will return false. 


**Optgroup**
- - - -
```html
<label for="favorite-food">Favorite Food</label>
<select name="favorite-food" id="favorite-food">
  <option value="">---Please Select a Food ---</option>
  <optgroup label="Italian">
      <option value="pizza">Pizza (Ninja Turtles)</option>
      <!-- Selected will be the default -->
      <option selected value="mushrooms">Shrooms (Mario)</option>
  </optgroup>
  <optgroup label="Sweets">
      <option value="doughnut"> Doughnuts (Homer)</option>
  </optgroup>
</select>
```
This will add like a title inside of the select box. 


### Additional Elements
- - - -
* range
* color
* date
* textarea
















