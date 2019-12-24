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

---

[9. Classes]:https://docs.python.org/3.7/tutorial/classes.html
