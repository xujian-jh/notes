# [5. Data Structures]

## 5.1. More on Lists

- list.append(x)
  - Add an item to the end of the list.
  - Equivalent to `a[len(a):] = [x]`.
- list.extend(iterable)
  - Extend the list by appending all the items from the iterable.
  - Equivalent to `a[len(a):] = iterable`.
- list.insert(i, x)
  - Insert an item at a given position. The first argument is the index of the element before which to insert,
    - so `a.insert(0, x)` inserts at the front of the list,
    - and `a.insert(len(a), x)` is equivalent to `a.append(x)`.
- list.remove(x)
  - Remove the first item from the list whose value is equal to x.
  - It raises a ValueError if there is no such item.
- list.pop([i])
  - Remove the item at the given position in the list, and return it.
  - If no index is specified, `a.pop()` removes and returns the last item in the list.
  - (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position.)
- list.clear()
  - Remove all items from the list.
  - Equivalent to `del a[:]`.
- list.index(x[, start[, end]])
  - Return zero-based index in the list of the first item whose value is equal to x.
    - Raises a ValueError if there is no such item.
  - The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list.
    - The returned index is computed relative to the beginning of the full sequence rather than the start argument.
- list.count(x)
  - Return the number of times x appears in the list.
- list.sort(key=None, reverse=False)
  - Sort the items of the list in place.
- list.reverse()
  - Reverse the elements of the list in place.
- list.copy()
  - Return a shallow copy of the list.
  - Equivalent to `a[:]`.

```s
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

- This is a design principle for all mutable data structures in Python.
  - You might have noticed that methods like `insert`, `remove` or `sort` that only modify the list have no return value printed – they return the default `None`.

### 5.1.1. Using Lists as Stacks

- Stack (“last-in, first-out”)
  - To add an item to the top of the stack, use `append()`.
  - To retrieve an item from the top of the stack, use `pop()` without an explicit index.

```s
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 5.1.2. Using Lists as Queues

- Queue (“first-in, first-out”)
  - lists are not efficient for this purpose. (because all of the other elements have to be shifted by one).
  - To implement a queue, use `collections.deque` which was designed to have fast appends and pops from both ends.

```s
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. List Comprehensions

- List comprehensions provide a concise way to create lists.
  - If the expression is a tuple (e.g. the `(x, y)` in the example), it must be parenthesized.
  - List comprehensions can contain complex expressions and nested functions.

```s
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 5.1.4. Nested List Comprehensions

```s
>>> matrix = [
...      [1, 2, 3, 4],
...      [5, 6, 7, 8],
...      [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(1)]
[[1, 5, 9]]
>>> [[row[i] for row in matrix] for i in range(2)]
[[1, 5, 9], [2, 6, 10]]
>>> [[row[i] for row in matrix] for i in range(3)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11]]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> [[row[i] for row in matrix] for i in range(5)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
  File "<stdin>", line 1, in <listcomp>
IndexError: list index out of range
```

- In the real world, you should prefer built-in functions to complex flow statements.
  - The `zip()` function would do a great job for this use case:

```s
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## 5.2. The `del` statement

- There is a way to remove an item from a list given its index instead of its value.

```s
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

## 5.3. Tuples and Sequences

- Sequence Types
  - Lists are mutable
  - Tuples are immutable
  - range

```s
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

## 5.4. Sets

- A set is an unordered collection with no duplicate elements.
  - Basic uses include membership testing and eliminating duplicate entries.
  - Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
- Curly braces or the `set()` function can be used to create sets.
  - Note: to create an empty set you have to use `set()`, not `{}`; the latter creates an empty dictionary, a data structure that we discuss in the next section.

```s
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

### 5.4.1. set comprehensions

```s
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 5.5. Dictionaries

- It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
  - A pair of braces creates an empty dictionary: `{}`.
  - Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

```s
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

### 5.5.1. The `dict()` constructor builds dictionaries directly from sequences of key-value pairs

```s
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

### 5.5.2. dict comprehensions

```s
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

## 5.6. Looping Techniques

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the `items()` method.

```s
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the `enumerate()` function.

```s
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

To loop over two or more sequences at the same time, the entries can be paired with the `zip()` function.

```s
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the `reversed()` function.

```s
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

To loop over a sequence in sorted order, use the `sorted()` function which returns a new sorted list while leaving the source unaltered.

```s
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

## 5.7. More on Conditions

- Note that in Python, unlike C, assignment cannot occur inside expressions.
  - it avoids a common class of problems encountered in C programs: typing `=` in an expression when `==` was intended.
- All comparison operators have the same priority, which is lower than that of all numerical operators.
  - The operators `is` and `is not` compare whether two objects are really the same object; this only matters for mutable objects like lists.
  - The comparison operators `in` and `not in` check whether a value occurs (does not occur) in a sequence.
- The Boolean operators `and` and `or` are so-called short-circuit operators.
  - their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.
  - `not` has the highest priority.

## 5.8. Comparing Sequences and Other Types

- Sequence objects may be compared to other objects with the same sequence type.
  - mixed numeric types are compared according to their numeric value, so `0` equals `0.0`, etc.
  - Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.
- The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted.
  - If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively.
  - If all items of two sequences compare equal, the sequences are considered equal.
  - If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one.
- Lexicographical ordering for strings uses the Unicode code point number to order individual characters.

---

[5. Data Structures]:https://docs.python.org/3.7/tutorial/datastructures.html
