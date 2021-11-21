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
