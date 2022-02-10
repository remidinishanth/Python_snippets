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

https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958

https://github.com/python/cpython/blob/main/Modules/_decimal/libmpdec/convolute.c

* a, b = b, a

```
print(1_000_000_000)  # 1000000000
print(1_234_567)  # 1234567

my_list = [1, 2, 3, 4]
print(my_list)  # [1, 2, 3, 4]
print(*my_list)  # 1 2 3 4
```

* `_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]`
* last element of list
* `list` can store any type of data, list pointing to itself
* `with` statement
* lru_cache
* reference-counting scheme with (optional) delayed detection of cyclically linked garbage


Awesome Internal things: https://rushter.com/blog/python-class-internals/


* Python Data Model https://docs.python.org/2/reference/datamodel.html 

A class has a namespace implemented by a dictionary object. Class attribute references are translated to lookups in this dictionary, e.g., `C.x` is translated to `C.__dict__["x"]` (although for new-style classes in particular there are a number of hooks which allow for other means of locating attributes). When the attribute name is not found there, the attribute search continues in the base classes.
