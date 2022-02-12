## TODO: https://www.programiz.com/article/python-self-why

Ref: https://rushter.com/blog/python-class-internals/

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

We can say that **changing class variables through class affect all instances**.

```python
c1 = Class()
c2 = Class()
print(c1.ClassVar, c2.ClassVar) # (0, 0)
Class.ClassVar = 3
print(c1.ClassVar, c2.ClassVar) # (3, 3)
```

Python creates a **new instance variable with the same name as a class variable** and instance variables have precedence over class variables when searching for an attribute value, hence the output i.e. value changes only for `c1.ClassVar`.

```python
c1 = Class()
c2 = Class()
print(c1.ClassVar, c2.ClassVar) # (0, 0)
c1.ClassVar = 3
# vars(c1) {'InstanceVar': 1, 'ClassVar': 3}
# vars(c2) {'InstanceVar': 1}
print(c1.ClassVar, c2.ClassVar) # (3, 0)
```

### Diamond Inheritance

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

### Overriding the attribute accessing methods


```python
class Attributes(object):
  def __getattr__(self, name):
    return self.__dict__[name] # or some other 
a = Attributes()
print(a.key) # It will print a.__dict__[key] 


class SuperSecretClass(object):
  def __getattribute__(self, name):
    return None 
a = SuperSecretClass()
print(a.key) # Always None


class Attributes(object):
  def __setattr__(self, name, value):
    if name == 'key':
      raise Exception('Not allowed!')
    self.__dict__[name] = value
a = Attributes()
a.key1 = None # Ok
a.key = None # Throws error 'Not allowed!'


class Attributes(object):
  def __delattr__(self, name):
    if name == 'key':
      raise Exception('Not allowed!')
    del self.__dict__[name]

a = Attributes()
a.key1 = None
a.key = None
del a.key1 # Ok
del a.key # Throws error 'Not allowed!'
```
