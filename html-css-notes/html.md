## HTML
- html is not supposed to be used to set the layout and vibe of the website.
- modern html is used to describe the content
    - you create the contents of the websites and to manipulate the website you would use CSS or javascript.

### Comments
``` html
<!-- this is how you write a comment! -->
use the [] cmd + / ] shortcut to turn a line into a comment.
```
- comments do stay apart of the document but do not render.
- so if the user inspects the website they can see the comments but the website itself does not include the comments.

### Tags
``` html
<div> this is a tag, note how there is an opening and closing tag. </div> 
``` 
- this is a div tag which just defines a content as a container. 

```html
<div>html does not respect spaces that the user inputs, 

    so when this page is rendered, the whitespace will not be included. 
</div>
```
- span: generic inline container, similar to div.
- h1
- h2
- p
- section

### how to write your html
- your html should follow the way your website will look.
- so if you have a footer section it is best placed at the bottom of the document although it could be placed anywhere in the document


### Nesting
``` html
<div>
    <p>
        this p element is a child of this div
    </p>
    <p>
        this is another child of this div. 
    </p>
</div>
```
- you can nest as much as you need. 

### Lists
```html
<ul>
    <li>
        list item
    </li>
</ul>
```
- ul works by nesting a li item inside of it. 

### Tables
- this is used for to represent information that is best used in a table
- so something that might look like will be used in a spreadsheet
- tables are not used for layout. 

### HR
- the hr tag is used for semantics not for styling
- this is similar like strong/bold tags. 
- this is for a thematic break like if you're writing a poem.
- a line reader will just read it as thematic break

### Attributes
```html
<a href="http://google.com"> Go to Google </a>

<img src="some sort of link path"/>
```
- this is an anchor tag and href is an attribute that contains a url.
    - this href tag can be used to link to local files 
- note how the attribute goes inside fo the a tag and it is wrapped around "< >"

- in this img tag, the src is an attribute and the link path or url will be the value.

- id attribute: 
    - each id will have its own unique value. 
    - this will be a problem bc with js and react will only select the first instance of that id

- class attribute:
    - this attribute sort of works like grouping content together.
    - you can also have multiple classes. 
    - the values will be alphanumeric and you should not start a value with a number. 
    - a standard is to do something called kebab case.
        - this is connecting a dash through multiple words. 

``` html
<div class="main-content first"></div>
```

### Block elements
- block level content will take up all of the allowed horizontal space

### Inline elements
- inline elements only take up the space needed for its content
- you can have inline elements inside of a block element 
``` html
<div> <strong> Honesty </strong> is the best policy. </div>
```

### Structure of HTML
- html tag
___
- head tag
    - title tag: located inside of the head tag and it is the name of the tab. 
        - if a title tag is not defined the default is the URL.

    - meta tag: all meta tags will have a name and content attribute. 

    - link tag: has a rel attribute which is relation and href to link the URL
        - rel stylesheet
        - rel icon (this is talking about favicon)
    - style tag: this is where you could put css 
    -script tag: this is where you could put js
___

- body tag
    - the body tag is what gets rendered.
    - div tag: used as some sort container to group content
        - header tag: you can put these items in the header:
            - h1 tag: webpage title
            - nav tag: navigation bar, can be placed in here but with css you can move this to the very top
                - this might be appealing to put under your page title so that the screen reader will say the title of the page first rather then the nav bar. 
                - the nav will have an "unordered list"
        - script tag:
    
