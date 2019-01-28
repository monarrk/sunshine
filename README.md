# sunshine
A low level, compiled language built to be small and fast that will probably never be finished.

### Syntax?
Here’s the basic idea:
```js
// hello world

fn main() int {
    // this is a comment
    println(“Hello world!”)
    return 0
}


// a more “advanced” example might be:

fn read(prompt) string {
    printf(“%s”, prompt)
    inp := readln()
    return inp
}```