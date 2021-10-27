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
