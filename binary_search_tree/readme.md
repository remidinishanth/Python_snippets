Both bst.py and avl.py (as well as bstsize.py) can be tested interactively from a UNIX shell as follows:

* `python bst.py 10` — do 10 random insertions, printing BST at each step
* `python avl.py 10` — do 10 random insertions, printing AVL tree at each step


Alternatively, you can use them from a Python shell as follows:

```python
>>> import bst
>>> t = bst.BST()
>>> print t

>>> for i in range(4):
...   t.insert(i);
...
>>> print t
0
/\
 1
 /\
  2
  /\
   3
   /\
>>> t.delete_min()
>>> print t
1
/\
 2
 /\
  3
  /\
```

  
```python
>>> import avl
>>> t = avl.AVL()
>>> print t

>>> for i in range(4):
...   t.insert(i);
...
>>> print t
  1
 / \
0  2
/\ /\
    3
    /\
>>> t.delete_min()
>>> print t
  2
 / \
1  3
/\ /\
```
