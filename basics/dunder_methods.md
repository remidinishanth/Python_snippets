## __str__ and __repr__

There is often confusion as to what the differences between these two built-ins are, but the difference is
simple and clear. The `str` class is used when you want to convert something to the string type, and is also
used when you need a readable representation of your object. On the other hand, the `repr` function is used
to create an unambiguous representation of its argument.

End users generally use `str` because they want to print readable and good looking text, whereas developers may use `repr` because they need to debug code and need to make sure they know what they are looking at. 

For example, take a look at the following interactive session:

```python
>>> print(3)
3
>>> print("3")
3
>>> 3
3
>>> "3"
'3'
```

The print function calls `str` on its argument and then displays it, so both the integer `3` and the string `"3"`
get printed the same way: you have no way to tell if the original object is an integer or a string. 

After that, you see that simply writing the integer `3` and the string `"3"` in the REPL returns an unambiguous representation of the object: you can tell integers and strings apart, because the REPL is using repr under the hood to show
objects.

```python
In [212]: class Sic(object):
     ...:     def __repr__(object): return 'foo'
     ...:

In [213]: str(Sic())
Out[213]: 'foo'

In [214]: repr(Sic())
Out[214]: 'foo'

In [215]: class Sic(object):
     ...:     def __str__(object): return 'foo'
     ...:

In [216]: str(Sic())
Out[216]: 'foo'

In [217]: repr(Sic())
Out[217]: '<__main__.Sic object at 0x7fad579e1c10>'
```

As you see, if you override `__repr__`, that's ALSO used for `__str__`, but not vice versa.



`__repr__`: representation of python object usually eval will convert it back to that object

`__str__`: is whatever you think is that object in text form

```python
In [218]: s="""w'o"w"""

In [219]: repr(s)
Out[219]: '\'w\\\'o"w\''

In [220]: str(s)
Out[220]: 'w\'o"w'

In [221]: eval(str(s))==s
Traceback (most recent call last):

  File "/Users/nishanth.reddy/miniconda3/lib/python3.8/site-packages/IPython/core/interactiveshell.py", line 3437, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)

  File "<ipython-input-221-2baed6d8daca>", line 1, in <module>
    eval(str(s))==s

  File "<string>", line 1
    w'o"w
        ^
SyntaxError: EOL while scanning string literal


In [222]: eval(repr(s))==s
Out[222]: True
```

`str(object='')`

```
Return a string containing a nicely printable representation of an object. 

For strings, this returns the string itself. 

The difference with repr(object) is that str(object) does not always attempt to return a string 
that is acceptable to eval(); its goal is to return a printable string. 

If no argument is given, returns the empty string, ''.
```

Built-in help for `repr`

```python
repr(...)
    repr(object) -> string

    Return the canonical string representation of the object.
    For most object types, eval(repr(object)) == object.
```

How is `__repr__` helpful?

Let's look at how useful it can be, using the Python shell and datetime objects. First we need to import the datetime module:

```python
import datetime
```

If we call datetime.now in the shell, we'll see everything we need to recreate an equivalent datetime object. This is created by the datetime `__repr__`:

```python
>>> datetime.datetime.now()
datetime.datetime(2015, 1, 24, 20, 5, 36, 491180)
```

If we print a datetime object, we see a nice human readable (in fact, ISO) format. This is implemented by datetime's `__str__`:

```python
>>> print(datetime.datetime.now())
2015-01-24 20:05:44.977951
```

source: https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
