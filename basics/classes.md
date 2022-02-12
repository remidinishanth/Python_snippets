## TODO: https://www.programiz.com/article/python-self-why

Also cover basics of `__new__` and metaclasses

```python
class Class:
  ClassVar = 0

  def __init__(self):
    self.InstanceVar = 1

  def func(self):
    return None

c = Class()
```

Use `dir(...)` and `vars(...)` to understand them better


```python
print(dir(Class))
# ['ClassVar', '__doc__', '__init__', '__module__', 'func']

print(vars(Class)) # or __dict__
# {'__module__': '__main__', 'ClassVar': 0, 'func': <function func at 0x0000000002C5AEB8>, '__init__': <function __init__ at 0x0000000002C5AE48>, '__doc__': None}
```

```python
print(dir(c))
# ['ClassVar', 'InstanceVar', '__doc__', '__init__', '__module__', 'func']


print(vars(c)) # or __dict__
# {'InstanceVar': 1}
```

```python
c1 = Class()
c2 = Class()
print(c1.ClassVar, c2.ClassVar) # (0, 0)
Class.ClassVar = 3
print(c1.ClassVar, c2.ClassVar) # (3, 3)
```

Python creates a new instance variable with the same name as a class variable and instance variables have precedence over class variables when searching for an attribute value, hence the output i.e. value changes only for `c1.ClassVar`.

```python
c1 = Class()
c2 = Class()
print(c1.ClassVar, c2.ClassVar) # (0, 0)
c1.ClassVar = 3
print(c1.ClassVar, c2.ClassVar) # (3, 0)
```



```python
class A(object):
  attr = 'A'

class B(A):
  pass
  
class C(A):
  attr = 'C'

class D(B, C):
  pass

d = D()

print(d.attr) # C

print(d.__class__.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>]
```
