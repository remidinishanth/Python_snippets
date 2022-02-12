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
