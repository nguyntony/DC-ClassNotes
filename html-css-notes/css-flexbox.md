- flexbox 

- before adding any styling (ie. adding display: flex) the content will go up and down. so if you have one parent with three children, the kids will go up and down. (it appears to go up and down like a column)

- if you go the parent and apply display: flex 
- what will happen is that, when you apply this the children will not go vertically anymore but will go horizontally. 
- there are two axis: 
    - main axis: this may change but you will know this by the way your content flows, so if your content flows horizontally then that's the main axis. 
    - cross axis: the other axis. 


- in the parent where you called display: flex, you now can use flex-direction: column which now will change the children to go vertically again. the main axis is now the vertical one. 

- in the parent (currently the main axis is the x axis)
- only display: flex is applied
    - justify-content: flex-start 
        - this is the default 
        - this will change the placement of the children, there is space-between and space-around, space-evenly. this will affect how the children is laid out on the main axis. 
    
    - align-items: 
        - center, flex-start, flex-end, stretch
        this will take our children and now align them vertically since our main axis is the x axis. 
        - stretch will stretch to the height of the parent but if the child has a set height, this will not take affect, 
    
    - flex-wrap: 
        - by default it will shrink the content to fit on one line
        - wrap: will respect the dimensions of the children (if they are established) and then will push any overflow child to the next line. 
            - the child jumps down to the next line but there may be a gap between the first and second line. to fix this you will use...
    
    - align-content: 
        - flex-start: this will move the child down and it will be next to one another. no gap between the first line and second.

    - text-align: 
        if there is text content inside of the parent then this will align the text content in the center.




- flex-direction: column ( the main axis will now be the y axis, therefore the properties we defined above will switch )
    - justify-content: 
        - this will now affect the content vertically 
    - align-items:
        - this will now affect the content horizontally now. 



in the children (flex is only one level deep so it will not apply to grandchildren, you will need to call display: flex in the children that you want in order to affect the grandchildren. 
- order: 
    - the default order is 0 and it will be rendered based on the html.
    - the lower the number the more first it will be.
    - the higher the number the further back it will be.
- flex-grow: 
    - if there is available empty space in the line of the children, a value of flex-grow: 1 will then make that child take up the remaining space available. 
    - this will be useful if you want all the children to be the same size but also take up any remaining space, this will overwrite any dimensions defined for the children. 
    - so as the browsers gets smaller or larger the children will grow or shrink accordingly. 
- flex-shrink:
    - opposite of flex-grow
-flex-basis:
    - this will be similar to the width property value and this will set a default width for the item. 
- align-self:
    - this will align the child itself to whatever you want. 



shorthand:
- flex-flow: combines the direction and wrap or not. 
    - flex-flow: column wrap;

- flex: 
    - flex: grow shrink basis
        - flex: 1 0 auto;
        - flex: 1 1 300px; 
            - you will need to apply this to all of the children in the parent container (if that is what you wanted to do) and what this will do is that when there is remaining whitespace the first value is grow so all of the children will grow to fill of that space, and the second value will make all the children shrink the same ratio and then the last value is flex-basis and what that does is that the width we give it is 300px so when it shrinks it will not got below 300px and it will then push the child to the next line. and when it is pushed to the next line, the child will then grow to take up the space of the new line.