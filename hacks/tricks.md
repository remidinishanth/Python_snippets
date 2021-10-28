### Locals

The `locals()` method updates and returns a dictionary of the current local symbol table.

A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.


```python
def make_complex(*args):
    x, y = args
    return dict(**locals())
    
# The above is same as

def make_complex(x, y):
    return {'x': x, 'y': y}
```

A Global symbol table stores all information related to the global scope of the program, and is accessed in Python using `globals()` method.

Read about namespaces at https://www.programiz.com/python-programming/namespace

![image](https://user-images.githubusercontent.com/19663316/139116283-e907f849-b33a-4280-aae6-0262a9d3e634.png)

```python
def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

## Ouput:
# a = 30
# a = 20
# a = 10
```

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

Decorators - This behaviour is the syntactic sugar because writing `@decorator` above the function definition is the same as calling `f = decorator(f)` after it.

```python
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''
```

Decarators can also take arguments.

```python
def prefix(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            return str(value) + str(r)
        return wrapper
    return decorator
    

@prefix('£')
def generate_bonus():
    return 250
    
generate_bonus()  # Ouput:  '£250'
```

```python
@f1(arg)
@f2
def func(): pass

# is roughly equivalent to

def func(): pass
func = f1(arg)(f2(func))
```

When using decorators, the wrapped function’s signature such as its `__name__` are lost and replaced by that of the wrapper function. To avoid this, `functools.wraps` comes into play.

```python
from functools import wraps
def money_format(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        formatted = '£{:.2f}'.format(r)
        return formatted
    return wrapper
```

REF: https://medium.com/python-monkey/function-decorators-74c08b9493bf


# Default Argument Gotchas / Dangers of Mutable Default arguments

```python
def foo(x=[]):
    x.append(1)
    print(x)
    
foo()  # [1]
foo()  # [1, 1]
foo()  # [1, 1, 1]
```

When Python executes a `def` statement, it takes some ready-made pieces (including the compiled code for the function body and the current namespace), and creates a new function object. When it does this, it also evaluates the default values.

You can use ` foo.__name__`, `foo.__code__`, `foo.__defaults__` and `foo.__globals__` to inspect more about the function.

```python
inspect.getfullargspec(foo)
# Output: FullArgSpec(args=['x'], varargs=None, varkw=None, defaults=([1, 1, 1],), kwonlyargs=[], kwonlydefaults=None, annotations={})
```

Instead, you should use a sentinel value denoting "not given" and replace with the mutable you'd like as default:

```python
def foo(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)
    
foo()  # [1]
foo()  # [1]
```

If you need to handle arbitrary objects (including None), you can use a sentinel object:

```python
sentinel = object()

def myfunc(value=sentinel):
    if value is sentinel:
        value = expression
    # use/modify value here
```

TODO: https://www.codingame.com/playgrounds/2302/best-tricks-of-python
