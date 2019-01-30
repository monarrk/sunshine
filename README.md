# sunshine
A low level, compiled language built to be small and fast that will probably never be finished.

### Syntax?
What can it do right now?
Basically, nothing. At the moment it can only print math. You can do this with
```go
println( {{ equation }} );
```

### Compile
There are currently a __lot__ of steps to compile, though soon that will change.
You also need the following dependancies installed:
1. llvm (for llc)
2. rply
3. gcc

Part 1:

    go to the directory
    
    run `python3 main.py test.sun`
    
Part 2:

    run `llc -filetype=obj output.ll`
    
Part 3:

    run `gcc -no-pie output.o -o output`
    
Part 4:

    run `./output`
