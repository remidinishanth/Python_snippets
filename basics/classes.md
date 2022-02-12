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
print(vars(Class)) # or __dict__


['ClassVar', '__doc__', '__init__', '__module__', 'func']
{'__module__': '__main__', 'ClassVar': 0, 'func': <function func at 0x0000000002C5AEB8>, '__init__': <function __init__ at 0x0000000002C5AE48>, '__doc__': None}
```

```python
print(dir(c))
print(vars(c)) # or __dict__


['ClassVar', 'InstanceVar', '__doc__', '__init__', '__module__', 'func']
{'InstanceVar': 1}
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

print(d.attr) ## C
print(d.__class__.mro())

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>]
```
