* Simple BST (no balancing)

  - `bst.py (PY)`  -> Features: insert, find, delete_min, ASCII art

  - `bstsize.py (PY)`  -> Imports and extends bst.py, Augmentation to compute subtree sizes

  - `bstsize_r.py (PY)`  -> Recursive version from recitation for computing subtree sizes, Features: insert, find, rank, delete


* AVL tree
  - `avl.py (PY)` -> Imports and extends bst.py, Features: insert, find, delete_min, ASCII art


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

source: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/
