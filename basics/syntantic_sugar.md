Syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express.

```python
‘name’ in my_list      ->      my_list.__contains__(‘name’)
len(my_list)           ->      my_list.__len__()
print(my_list)         ->      my_list.__repr__()
my_list == “value”     ->      my_list.__eq__(“value”)
my_list[7]             ->      my_list.__getitem__(7)
my_list[-1]            ->      my_list[len(my_list) - 1]
```

```python
@decorator # syntax    ->      func = decorator(func)
```

```python
1 < x < 10
# equivalent to 1 < x and x < 10

[x for x in range(10)] 
# List comprehension

{key: value for key, value in d.items()}
# Dict comprehension

x = something if condition else otherthing
# python ternary

big_number = 1_000_000_000
# equivalent to big_number = 1000000000

a += 1
# equivalent to a = a + 1

x = something if condition else otherthing
# Ternary operator

# List “Multiplication”
>>> mylist = [1,2,3,4]
>>> mylist *= 4
>>> print(mylist)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
```

* Attribute access in Python - `obj.attr` is syntax for `getattr(obj, "attr")`.

Attribute access on an object is implemented via two special methods. The first method is `__getattribute__()` which is called when trying to access any and all attributes. The second is `__getattr__()` which is called when `__getattribute__()` raises an `AttributeError`. The former method is (nowadays) always expected to be defined while the latter method is optional.

![image](https://user-images.githubusercontent.com/19663316/139597874-e9e323e6-e9e5-4e7c-b0ca-6383ce751009.png)


```python
stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))
```

In this code, we call the `__getitem__` method in the `list` class and pass the list and the item we want retrieved from the list as parameters.

* The sixth line calls the `__getitem__()` method in the `stuff` list with a parameter of `0` --> `stuff.__getitem__(0)`
* The seventh line is an even more verbose way of retrieving the `0`-th item in the list --> `list.__getitem__(stuff,0)`

The last three lines of the program are equivalent, but it is more convenient to simply use the square bracket syntax to look up an item at a particular position in a list.


* `import a` syntactic sugar
```python
a = __import__("a", globals(), locals())

# import a.b
a = __import__("a.b", globals(), locals())

# from a.b import c
c = __import__('a.b', globals(), locals(), ['c']).c

# from ..a import b, relative import, essentially involves counting
b = __import__('a', globals(), locals(), ['b'], 2).b

# import a as b
b = __import__("a", globals(), locals())

# from .a import b as c
c = __import__('a', globals(), locals(), ['b'], 1).b
```

* `for ...`

The statements in the else block are executed if execution falls off the bottom of the try - if there was no exception.

```python
for a in b:
    c
    

_iter = iter(b)
while True:
    try:
        a = next(_iter)
    except StopIteration:
        break
    else:
        c
del _iter
```    

* async with
```python
async for a in b:
    c
else:
    d
    
    
    
_iter = aiter(b)
_looping = True
while _looping:
    try:
        a = await anext(_iter)
    except StopAsyncIteration:
        _looping = False
        continue
    else:
        c
else:
    d
del _iter, _looping
```

TODO: https://snarky.ca/tag/syntactic-sugar/ and https://github.com/brettcannon/desugar
