```python
‘name’ in my_list      ->      my_list.__contains__(‘name’)
len(my_list)           ->      my_list.__len__()
print(my_list)         ->      my_list.__repr__()
my_list == “value”     ->      my_list.__eq__(“value”)
my_list[7]             ->      my_list.__getitem__(7)
```
