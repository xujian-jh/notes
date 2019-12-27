# [9. Classes]

## 9.1. A Word About Names and Objects

- Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object.
  - Aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types.
  - This is usually used to the benefit of the program, since aliases behave like pointers in some respects.

## 9.2. Python Scopes and Namespaces

- At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:
  - the innermost scope, which is searched first, contains the local names
  - the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
  - the next-to-last scope contains the current module’s global names
  - the outermost scope (searched last) is the namespace containing built-in names

## 9.3. A First Look at Classes

### 9.3.1. Class Definition Syntax

```s
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

- Class definitions, like function definitions (def statements) must be executed before they have any effect.
- In practice, the statements inside a class definition will usually be function definitions.
- When a class definition is entered, a new namespace is created, and used as the local scope.
- When a class definition is left normally (via the end), a class object is created.
  - This is basically a wrapper around the contents of the namespace created by the class definition.

### 9.3.2. Class Objects

- Class objects support two kinds of operations: attribute references and instantiation.
  - Attribute references use the standard syntax used for all attribute references in Python: `obj.name`.
    - Valid attribute names are all the names that were in the class’s namespace when the class object was created.
  - Class instantiation uses function notation.
    - Just pretend that the class object is a parameterless function that returns a new instance of the class.

```s
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3. Instance Objects

- The only operations understood by instance objects are attribute references.
  - There are two kinds of valid attribute names, data attributes and methods.
    - A method is a function that “belongs to” an object.

```s
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

So in our example, `x.f` is a valid method reference, since `MyClass.f` is a function, but `x.i` is not, since `MyClass.i` is not. But `x.f` is not the same thing as `MyClass.f` — it is a method object, not a function object.

### 9.3.4. Method Objects

If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object.

```s
x.f()
```

- Usually, a method is called right after it is bound.
  - In the MyClass example, this will return the string 'hello world'.

```s
xf = x.f
while True:
    print(xf())
```

- However, it is not necessary to call a method right away: `x.f` is a method object, and can be stored away and called at a later time.
  - In the MyClass example, this will continue to print hello world until the end of time.

### 9.3.5. Class and Instance Variables

- instance variables are for data unique to each instance
- class variables are for attributes and methods shared by all instances of the class.

## 9.4. Random Remarks

- it is all based upon convention, to avoid accidental name conflicts.
  - Data attributes override method attributes with the same name.
  - Data attributes may be referenced by methods as well as by ordinary users (“clients”) of an object.

## 9.5. Inheritance

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

## 9.6. Private Variables

- “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.
  - However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. `_spam`) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.
  - Any identifier of the form `__spam` is textually replaced with `_classname__spam`, where classname is the current class name.

## 9.9. Generators

- Generators are a simple and powerful tool for creating iterators.
  - They are written like regular functions but use the `yield` statement whenever they want to return data.
  - Each time `next()` is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

```s
>>> def reverse(data):
...     for index in range(len(data)-1, -1, -1):
...         yield data[index]
...
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

## 9.10. Generator Expressions

Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

```s
>>> sum(i*i for i in range(10))                 # sum of squares
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260
```

---

[9. Classes]:https://docs.python.org/3.7/tutorial/classes.html
