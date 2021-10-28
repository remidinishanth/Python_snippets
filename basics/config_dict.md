## 1
Updating the module dictionary so that we can use config.VAR_NAME while accessing the variable

```python
# Inside config.py
import sys

import yaml


def load_config(config_file):
    _module = sys.modules[__name__]
    with open(config_file) as gw_config:
        config_dict = yaml.safe_load(gw_config)
        _module.__dict__.update(config_dict)
```


Read more at https://stackoverflow.com/questions/5365562/why-is-the-value-of-name-changing-after-assignment-to-sys-modules-name

## 2
Using SimpleNamespace

```python
>>> from types import SimpleNamespace
>>> d = {'key1': 'value1', 'key2': 'value2'}
>>> n = SimpleNamespace(**d)
>>> print(n)
namespace(key1='value1', key2='value2')
>>> n.key2
'value2'
```

Adding, modifying and removing values is achieved with regular attribute access, i.e. you can use statements like `n.key = val` and `del n.key`.

To go back to a dict again:

```python
>>> vars(n)
{'key1': 'value1', 'key2': 'value2'}
```

source: https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python

## 3
Nested get using dot convention, source: https://github.com/robertchase/ergaleia/blob/master/ergaleia/nested_get.py

```python
def nested_get(d, keys, default=None, required=False, as_list=False):
    """ Multi-level dict get helper
        Parameters:
            d        - dict instance
            keys     - iterable of keys or dot-delimited str of keys (see
                       Note 1)
            default  - value if index fails
            required - require every index to work (see Note 2)
            as_list  - return result as list (see Note 3)
        Notes:
            1. Each key is used to index a dict, replacing the dict with
               the matching value. This process is repeated until an index
               fails, or the keys are exhausted.
               If keys is a string, it is split by '.' and treated as a
               list of keys.
            2. If the required flag is False, a failure to match a key
               causes the default value to be used. If the required flag is
               True, every key must match, otherwise a TypeError or KeyError is
               raised.
            3. If as_list is True, a non-list match will be wrapped in a list,
               unless match is None, which will be replaced with an empty list.
    """
    if isinstance(keys, str):
        keys = keys.split('.')
    for key in keys:
        try:
            d = d[key]
        except KeyError:
            if required:
                raise
            d = default
            break
        except TypeError:
            if required:
                raise
            d = default
            break
    if as_list:
        return [] if d is None else [d] if not isinstance(d, list) else d
    return d
    
# Usage
class TestNestedGet(TestCase):

    def test_nested_get(self):
        data = {'a': {'b': {'c': 10}}}
        self.assertEqual(nested_get(data, 'a.b.c'), data['a']['b']['c'])
        self.assertEqual(nested_get(data, 'a.b.d', default='ok'), 'ok')
        self.assertIsNone(nested_get(data, 'a.b.d'))
        data = {'a': {'b': [1, 2]}}
        self.assertIsNone(nested_get(data, 'a.b.c'))
```

## 4

Using dot while accesing dict variables

```python
class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

mydict = {'val':'it works'}
nested_dict = {'val':'nested works too'}
mydict = dotdict(mydict)
mydict.val
# 'it works'

mydict.nested = dotdict(nested_dict)
mydict.nested.val
# 'nested works too'
```

source: https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary, Check other answers too
