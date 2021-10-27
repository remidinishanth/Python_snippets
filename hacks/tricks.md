### Argument Unpacking

You can unpack a list or a dictionary as function arguments using `*` and `**`.

```python
def draw_point(x, y):

# do some magic
point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)
```

Very useful shortcut since lists, tuples and dicts are widely used as containers.

### Chaining Comparison Operators

```python
In [1]: x = 5

In [2]: 1 < x < 10
Out[2]: True

In [3]: 10 < x < 20
Out[3]: False

In [4]: x < 10 < x*10 < 100
Out[4]: True

In [5]: 10 > x <= 9
Out[5]: True

In [6]: 5 == x > 4
Out[6]: True
```

### Decorators

Decorators allow to wrap a function or method in another function that can add functionality, modify arguments or results, etc. You write decorators one line above the function definition, beginning with an "at" sign (@).

```python
def print_args(function):
    def wrapper(*args, **kwargs):
        print('Arguments:', args, kwargs)
        return function(*args, **kwargs)
    return wrapper
    
@print_args
def write(text):
    print(text)
    
write('foo')

# Output:
# Arguments: ('foo',) {}
# foo
 ````

In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.

```python

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)

## Output:
## HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
## hi, i am created by a function passed as an argument.
```

```python
# Python program to illustrate functions
# Functions can return another function
 
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))
```

Decorators

```python
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''
```
