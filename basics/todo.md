https://pretagteam.com/question/why-is-a-class-dict-a-mappingproxy


https://stackoverflow.com/questions/32720492/why-is-a-class-dict-a-mappingproxy

dictproxy became mappingproxy https://docs.python.org/3.3/whatsnew/3.3.html#types

https://www.reddit.com/r/learnpython/comments/59m8fo/what_is_mappingproxy/

https://codesachin.wordpress.com/2016/06/09/the-magic-behind-attribute-access-in-python/

https://github.com/santiagobasulto/pycon-concurrency-tutorial-2020

TODO: https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.pdf

https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do?rq=1

https://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html

Yield method https://hackernoon.com/the-magic-behind-python-generator-functions-bc8eeea54220 and https://haldir65.github.io/2018/11/11/2018-11-11-python-gil-and-what-you-can-do-about-it/ and https://nedbatchelder.com/text/iter.html

![image](https://user-images.githubusercontent.com/19663316/153640732-a2744c88-e42d-4a5c-96ab-28744e2ae01f.png)

Magic ability for functions to freeze in the middle of execution and resume later, it enables us to implement coroutines and iterators almost effortlessly.

![image](https://user-images.githubusercontent.com/19663316/153641976-9de92cd7-6a17-4967-bafa-e6df31d4b47e.png)


https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958

https://github.com/python/cpython/blob/main/Modules/_decimal/libmpdec/convolute.c

* Dynamic typing. It stores that value at some memory location and then binds that variable name to that memory container.
* parallel assignment `a, b = b, a`

```
print(1_000_000_000)  # 1000000000
print(1_234_567)  # 1234567

my_list = [1, 2, 3, 4]
print(my_list)  # [1, 2, 3, 4]
print(*my_list)  # 1 2 3 4
```

* `_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]`
* last element of list, `my_list[-1]`
* `list` can store any type of data, list pointing to itself
* `with` statement
* lru_cache
* An assignment statement creates a symbolic name that you can use to reference an object. The statement `x = 'foo'` creates a symbolic name `x` that refers to the string object 'foo'. Ref: https://realpython.com/python-namespaces-scope/
* object model, reference-counting scheme with (optional) delayed detection of cyclically linked garbage

* Ease of Learning, Rapid Development Cycle. What makes Python awesome - Raymond
* import antigravity

Awesome Internal things: https://rushter.com/blog/python-class-internals/

* `globals()` Returns the `__dict__` of the calling module (i.e., the dictionary used as the global
namespace at the point of call). 

Good talk `The Python Datamodel: When and how to write objects`

* Python Data Model https://docs.python.org/2/reference/datamodel.html 

A class has a namespace implemented by a dictionary object. Class attribute references are translated to lookups in this dictionary, e.g., `C.x` is translated to `C.__dict__["x"]` (although for new-style classes in particular there are a number of hooks which allow for other means of locating attributes). When the attribute name is not found there, the attribute search continues in the base classes.

```
The starting point for descriptor invocation is a binding, a.x. How the arguments are assembled depends on a:

Direct Call
The simplest and least common call is when user code directly invokes a descriptor method: x.__get__(a).

Instance Binding
If binding to an object instance, a.x is transformed into the call: type(a).__dict__['x'].__get__(a, type(a)).

Class Binding
If binding to a class, A.x is transformed into the call: A.__dict__['x'].__get__(None, A).

Super Binding
If a is an instance of super, then the binding super(B, obj).m() searches obj.__class__.__mro__ for the base class A immediately following B and then invokes the descriptor with the call: A.__dict__['m'].__get__(obj, obj.__class__).
```

REF: https://docs.python.org/3/reference/datamodel.html#invoking-descriptors

* https://medium.com/geekculture/10-amazing-facts-i-bet-you-didnt-know-about-python-programming-language-e5d426fabf13


* Python objects are heap allocated and are not contiguous, nolocality, they are also huge(lot of overhead to store type, reference count, fixed bit integers etc), it's gonna use lot of memory.
