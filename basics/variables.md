![image](https://user-images.githubusercontent.com/19663316/139731226-e5af82f1-c2b6-4948-8605-36aadae8ed5e.png)

* Assignment never copies data.

![image](https://user-images.githubusercontent.com/19663316/139731384-92c60447-c1e6-4d7e-b4ae-98f358d817d4.png)

![image](https://user-images.githubusercontent.com/19663316/139731518-1ae6b906-4b66-422d-9feb-0f766b0c950f.png)

![image](https://user-images.githubusercontent.com/19663316/139189701-19010899-cec6-49c2-8bea-4bd012420e66.png)

![image](https://user-images.githubusercontent.com/19663316/139728336-6e63cdb6-dbc9-47ca-803d-89d36ba1778e.png)

![image](https://user-images.githubusercontent.com/19663316/139728553-393bdb3a-c0a3-4b10-a507-93bfe47e837c.png)

* In python, think in terms of "names", "bindings" and "objects".

```python
>>> dict = {'a':1,'b':2}
>>> list = dict.values()
>>> list
[1, 2]
>>> dict['a']=3
>>> list
[1, 2]
>>> dict
{'a': 3, 'b': 2}

# If you have lists

In [1]: dict = {'a':[1],'b':[2]}

In [2]: list = dict.values()

In [3]: list
Out[3]: dict_values([[1], [2]])

In [4]: dict['a'].append(3)

In [5]: dict
Out[5]: {'a': [1, 3], 'b': [2]}

In [6]: list
Out[6]: dict_values([[1, 3], [2]])
```

```
First, some terminology.  Actually, the very first thing is some
anti-terminology; I find the word "variable" to be particularly
uphelpful in a Python context.  I prefer "names", "bindings" and
"objects".

Names look like this:

    ,-----.
    | foo |
    `-----'

Names live in namespaces, but that's not really important for the
matter at hand as the only namespace in play is the one associated
with the read-eval-print loop of the interpreter.  In fact names are
only minor players in the current drama; bindings and objects are the
real stars.

Bindings look like this:

    ------------>

Bindings' left ends can be attached to names, or other "places" such
as attributes of objects and entries in lists or dictionaries.  Their
right hand ends are always attached to objects[[2]](http://python.net/crew/mwh/hacks/objectthink.html).

Objects look like this:

    +-------+
    | "bar" |
    +-------+
```

```
dict = {'a':1,'b':2}

After this statement, it would seem appropriate to draw this picture:

    ,------.       +-------+
    | dict |------>|+-----+|     +---+
    `------'       || "a" |+---->| 1 |
                   |+-----+|     +---+
                   |+-----+|     +---+
                   || "b" |+---->| 2 |
                   |+-----+|     +---+
                   +-------+
                   
list = dict.values()

Now this:

    ,------.       +-------+
    | dict |------>|+-----+|             +---+
    `------'       || "a" |+------------>| 1 |
                   |+-----+|             +---+
                   |+-----+|              /\
                   || "b" |+-----.    ,---'
                   |+-----+|     |    |
                   +-------+     `----+----.
                                      |    |
    ,------.       +-----+            |    \/
    | list |------>| [0]-+------------'   +---+
    `------'       | [1]-+--------------->| 2 |
                   +-----+                +---+

dict['a']=3

Now this:


    ,------.       +-------+
    | dict |------>|+-----+|             +---+
    `------'       || "a" |+-.           | 1 |
                   |+-----+| |           +---+
                   |+-----+| |            /\
                   || "b" |+-+---.    ,---'
                   |+-----+| |   |    |
                   +-------+ |   `----+----.
                             |        |    |
    ,------.       +-----+   |        |    \/
    | list |------>| [0]-+---+--------'   +---+
    `------'       | [1]-+---+----------->| 2 |
                   +-----+   |            +---+
                             |            +---+
                             `----------->| 3 |
                                          +---+


list # [1, 2]

dict # {'a': 3, 'b': 2}
```

The objects returned by `dict.keys()`, `dict.values()` and `dict.items()` are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

```
> >>> dict = {'a':[1],'b':[2]}

    ,------.       +-------+
    | dict |------>|+-----+|     +-----+   +---+
    `------'       || "a" |+---->| [0]-+-->| 1 |
                   |+-----+|     +-----+   +---+
                   |+-----+|     +-----+   +---+
                   || "b" |+---->| [0]-+-->| 2 |
                   |+-----+|     +-----+   +---+
                   +-------+

> >>> list = dict.values()

    ,------.       +-------+
    | dict |------>|+-----+|             +-----+   +---+
    `------'       || "a" |+------------>| [0]-+-->| 1 |
                   |+-----+|             +-----+   +---+
                   |+-----+|               /\
                   || "b" |+-----.    ,----'
                   |+-----+|     |    |
                   +-------+     `----+-----.
                                      |     |
    ,------.       +-----+            |     \/
    | list |------>| [0]-+------------'   +-----+   +---+
    `------'       | [1]-+--------------->| [0]-+-->| 2 |
                   +-----+                +-----+   +---+

> >>> list
> [[1], [2]]

Again, no surprises here.

> >>> dict['a'].append(3)

                                                    +---+
    ,------.       +-------+                     ,->| 1 |
    | dict |------>|+-----+|             +-----+ |  +---+
    `------'       || "a" |+------------>| [0]-+-'
                   |+-----+|             | [1]-+-.
                   |+-----+|             +-----+ |  +---+
                   || "b" |+-----.         /\    `->| 3 |
                   |+-----+|     |    ,----'        +---+
                   +-------+     |    |
                                 `----+-----.
    ,------.       +-----+            |     \/
    | list |------>| [0]-+------------'   +-----+   +---+
    `------'       | [1]-+--------------->| [0]-+-->| 2 |
                   +-----+                +-----+   +---+

> >>> dict
> {'a': [1, 3], 'b': [2]}
> >>> list
> [[1, 3], [2]]
```

![image](https://user-images.githubusercontent.com/19663316/139728487-c8d48484-24e9-47c4-919b-6427a53941bb.png)

![image](https://user-images.githubusercontent.com/19663316/139728752-a00e9d19-e0a4-468a-80cb-62eb884bc814.png)

![image](https://user-images.githubusercontent.com/19663316/139728978-d69a055c-a781-47d3-96da-d8ee70cbe7bc.png)

![image](https://user-images.githubusercontent.com/19663316/139729797-d83aacd6-5de0-4c58-b53f-ab9d289fbca8.png)

![image](https://user-images.githubusercontent.com/19663316/139729846-b77ff883-72ec-4957-9661-6f6355b5ce47.png)

![image](https://user-images.githubusercontent.com/19663316/139729939-60a905ba-cd86-46a1-a800-35d402169ebb.png)

![image](https://user-images.githubusercontent.com/19663316/139731015-b727088a-df2a-40e0-aafb-0df0242dbf6b.png)

![image](https://user-images.githubusercontent.com/19663316/139730597-ffa92bbb-81e0-4bd6-a3ed-af2bdc5680b9.png)

```python
board = [[0]*8]*8

board1 = [[0]*8 for _ in range(8)]
```

![image](https://user-images.githubusercontent.com/19663316/139730525-23758126-7627-4b3d-a614-bb63db70e5e0.png)

source: Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015, https://nedbatchelder.com/text/names.html

TODO: https://mathspp.com/blog/pydonts/inner-workings-of-sequence-slicing

When comparing `strings`, `int` literals it is adviced to use `==`: 
* `is` checks for identity - if the two variables point to the exact same object.
* `==` checks for equality - if the two variables point at values are equal. That is, if they will act the same way in the same situations.
source: https://adamj.eu/tech/2020/01/21/why-does-python-3-8-syntaxwarning-for-is-literal/

![image](https://user-images.githubusercontent.com/19663316/141359782-23073554-c8f2-4653-91da-1a295898072a.png)

source: http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#index-2

![image](https://user-images.githubusercontent.com/19663316/141359942-59842d9c-6229-4a3d-8330-485a60a88610.png)

Pure functions and Modifiers:
* pure function: A function that does not modify any of the objects it receives as arguments. Most pure functions are fruitful.
* modifier: A function that changes one or more of the objects it receives as arguments. Most modifiers are fruitless.
* functional programming style: A style of program design in which the majority of functions are pure.

![image](https://user-images.githubusercontent.com/19663316/141360546-1aebda3a-4610-4028-bd8c-e17dc0d7466d.png)
