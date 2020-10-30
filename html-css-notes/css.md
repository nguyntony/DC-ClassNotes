## CSS
- cascading style sheet. 

### Rule 
``` css
h1 {
    property1: value1;
    property2: value2;
    color: red;
}
```
- you start by declaring what element you want to interact with
- the opening curly bracket
- the property you wish to manipulate like background, font-size
- followed by a colon: and the value you want to use
- after each declaration there needs to be a semicolon
- ending curly bracket

### Selector Types
___
### tag selector

- if you want to select a tag you state the tag name
- if you wanted to select all span tags you do:
``` css
span {
    background: yellow;
}
```
### class selector
- to select element by classes you start with a .
``` css
.classname {
    color: red;
}
```

### id selector
- it is not best practice to use the id selector bc this will only ever affect one item
- the idea is, to write less code to do more things


### psuedo selector
``` css
h1:hover{

}

.nav-link:first-child {

}
```

### specificity 
- css follows this rule, whatever is the most specific 

### box model
- every item in a html document is a box. 
- content is in the center
- padding surrounds the content
    - padding: val val val val
        - top right bottom left
    - padding: val val val
        - top right&left bottom
    - paddding: val val
        - top&bottom
        - left&right
    - padding: val
        - all around
- border surrounds padding 
- margin surrounds border
    - background color does not include margin

### position
- relative:
    - by adding relative, by itself it doesn't do anything but you can add top left right bottom
    - it will move from its initial position
- fixed: similar to absolute but as you scroll this item will remain constant on the screen
    - 
- absolute: 
    - takes the item out of the regular flow and positions it based on what values you give it.
    - it will move from the viewport.  
- sticky: 
    - starts where it is defined but after the scrolling starts, it will remain at top.

### Flexbox
- 

### External CSS Libraries
- 