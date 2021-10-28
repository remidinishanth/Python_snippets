```python
‘name’ in my_list      ->      my_list.__contains__(‘name’)
len(my_list)           ->      my_list.__len__()
print(my_list)         ->      my_list.__repr__()
my_list == “value”     ->      my_list.__eq__(“value”)
my_list[7]             ->      my_list.__getitem__(7)
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


# List “Multiplication”
>>> mylist = [1,2,3,4]
>>> mylist *= 4
>>> print(mylist)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
```
