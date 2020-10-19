# Loops
- While loops
    - while loops, loop over something WHILE that condition is true.
    ```python
    i = 0 
    while i < 10:
        print(i)
        i =+ 1
    ```
    - we have assigned i a value of 0
    - this loop will increment i and also print i until i is greater than 10 
    - it stops then because the condition has turned to false.
    ```python
    on = True
    while on:
        choice = input("Do you want to keep going? ")
        if choice == "yes":
            print("okay!")
        else:
            on = False
    ```


- Infinite loops
    - infinite loops, loop over something FOREVER!
    ```python
    i = 0
    while True:
        print(i)
        i += 1
    ```
    - Instead of passing a condition we just gave it True.
    - There isn't a expressin or condition to turn False so this loop runs forever.
    - I don't think this is good. CTRL-C to stop it.


