Ariel Ortiz - The Perils of Inheritance: Why We Should Prefer Composition - PyCon 2019

source: https://github.com/ariel-ortiz/pycon2019_perils_of_inheritance/

![image](https://user-images.githubusercontent.com/19663316/140602276-85f33608-d8a8-4b29-b00b-270e4473f91e.png)

![image](https://user-images.githubusercontent.com/19663316/140602282-2f2068b4-567a-416b-bb27-0c28bbe2f9b6.png)

Advantages of Inheritance
* Easy way to reuse code
* Allows changing inherited implementation

Disadvantage of Inheritance
* The relationship between a base class and a derived calss is statically fixed
* Inheritance supports weak encapsulation and fragile structures
* A derived class inherits everything, even things it doesn't need or want
* Changes in a base class interface impact all its derived classes

![image](https://user-images.githubusercontent.com/19663316/140602572-1550481a-52da-4d56-9d71-691be7ae61d9.png)

```python
class LinkedList:

    class Node:

        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.header = LinkedList.Node()
        self.length = 0

    def insert(self, value):
        new_node = LinkedList.Node(value)
        new_node.next = self.header.next
        self.header.next = new_node
        self.length += 1

    def insert_all(self, iterable):
        for value in iterable:
            new_node = LinkedList.Node(value)
            new_node.next = self.header.next
            self.header.next = new_node
            self.length += 1

    def remove(self):
        if self.header.next is None:
            raise RuntimeError("Can't remove element from an empty list.")
        node = self.header.next
        self.header.next = node.next
        self.length -= 1
        return node.value

    def clear(self):
        self.length = 0
        self.header.next = None

    def __iter__(self):
        current = self.header.next
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return f"[{', '.join(str(value) for value in self)}]"

    def __len__(self):
        return self.length
```

`InsertCounter` using inheritance, this works as expected.

```python
from linked import LinkedList
from itertools import tee


class InsertCounter(LinkedList):

    def __init__(self):
        super().__init__()
        self._counter = 0

    def insert(self, value):
        super().insert(value)
        self._counter += 1

    def insert_all(self, iterable):
        iter1, iter2 = tee(iterable)
        super().insert_all(iter1)
        self._counter += sum(1 for _ in iter2)

    @property
    def counter(self):
        return self._counter
	

lst = InsertCounter()
lst.insert(4)
lst.insert_all([8, 15, 16, 23, 42])
lst.remove()
print(lst)
print(f'length  = {len(lst)}')
print(f'counter = {lst.counter}')
```


If we look at `LinkedList`, there is common code between `insert` and `insert_all` methods, we can modify the code to reuse `insert`. Modifying the base class breaks the derived class.

![image](https://user-images.githubusercontent.com/19663316/140602427-30bee154-c143-442d-bd19-8befd97ea104.png)

```python
    def insert_all(self, iterable):
        for value in iterable:
            self.insert(value)
```

It breaks the code because `self.insert(value)` calls the `insert` of Dervied class first.


To avoid this it is better if we use composition

![image](https://user-images.githubusercontent.com/19663316/140602589-3c853369-b566-4a04-aeef-890c9054a5cc.png)


```python
from linked import LinkedList
from itertools import tee


class InsertCounter:

    def __init__(self, linked_list):
        self.linked_list = linked_list
        self._counter = 0

    def insert(self, value):
        self.linked_list.insert(value)
        self._counter += 1

    def insert_all(self, iterable):
        iter1, iter2 = tee(iterable)
        self.linked_list.insert_all(iter1)
        self._counter += sum(1 for _ in iter2)

    @property
    def counter(self):
        return self._counter

    def remove(self):
        return self.linked_list.remove()

    def clear(self):
        self.linked_list.clear()

    def __iter__(self):
        return self.linked_list.__iter__()

    def __str__(self):
        return self.linked_list.__repr__()

    def __len__(self):
        return self.linked_list.__len__()


lst = InsertCounter(LinkedList())
lst.insert(4)
lst.insert_all([8, 15, 16, 23, 42])
lst.remove()
print(lst)
print(f'length  = {len(lst)}')
print(f'counter = {lst.counter}')
```

Advantages of Composition
* Implementations are configurable at runtime
* Supports good encapsulation and adaptable structures
* Interface changes have limited ripple effect
* Composition allows a composite class to hace relationships with many component classes

Disadvantages of Composition
* Frequently requires more code than inheritance
* Often more difficult to read than inheritance


When to use inheritance
* When the base and derived classes are in the same module/package and under the control of the same programmers
* When extending classes specifically designed and documented for extension


Things to Note
* Inheritance is not wrong
* Only use inheritance when a new class really does define a subtype of an existing class
* Inheritance and composition are not competitors
* Design and document for inheritance `JSONEncoder`. Example: https://docs.python.org/3/library/json.html#json.JSONEncoder
* When using inheritance never forget the Liskov Substituion Principle(LSP) - functions that use references to base class objects must be able to use objects of derived classes without knowing it.

![image](https://user-images.githubusercontent.com/19663316/140602782-0e007bfc-0924-432d-ade9-9ac010e38209.png)
