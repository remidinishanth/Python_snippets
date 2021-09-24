# In object-oriented programming, a metaclass is a class whose instances are classes

# When we define a class, the objects of that class are created using the class as the blueprint.

# For example, the following metaclass code sample adds a hello property 
# to each class which uses this metaclass as its template. 
# This means, new classes that are instances of this metaclass will 
# have a hello property without needing to define one themselves.

# hello_metaclass.py
# A simple metaclass
# This metaclass adds a 'hello' method to classes that use the metaclass
# meaning, those classes get a 'hello' method with no extra effort
# the metaclass takes care of the code generation for us
class HelloMeta(type):
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls

# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

# Create an instance of the metaclass. It should automatically have a hello method
# even though one is not defined manually in the class
# in other words, it is added for us by the metaclass
greeter = TryHello()
greeter.greet()
