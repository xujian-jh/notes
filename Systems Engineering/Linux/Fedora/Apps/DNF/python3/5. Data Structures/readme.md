# 5. [Data Structures]

## 5.1. More on Lists

- list.append(x)
  - Add an item to the end of the list.
  - Equivalent to a[len(a):] = [x].
- list.extend(iterable)
  - Extend the list by appending all the items from the iterable.
  - Equivalent to a[len(a):] = iterable.
- list.insert(i, x)
  - Insert an item at a given position.
  - The first argument is the index of the element before which to insert,
    - so a.insert(0, x) inserts at the front of the list,
    - and a.insert(len(a), x) is equivalent to a.append(x).
- list.remove(x)
  - Remove the first item from the list whose value is equal to x.
  - It raises a ValueError if there is no such item.
- list.pop([i])
  - Remove the item at the given position in the list, and return it.
    - The square brackets around the `i` in the method signature denote that the parameter is optional, not that you should type square brackets at that position.
    - If no index is specified, a.pop() removes and returns the last item in the list.
- list.clear()
  - Remove all items from the list.
  - Equivalent to del a[:].
- list.index(x[, start[, end]])
  - Return zero-based index in the list of the first item whose value is equal to x.
  - Raises a ValueError if there is no such item.
  - The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list.
    - The returned index is computed relative to the beginning of the full sequence rather than the start argument.
- list.count(x)
  - Return the number of times x appears in the list.
- list.sort(key=None, reverse=False)
  - Sort the items of the list in place
  - key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).
  - reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
- list.reverse()
  - Reverse the elements of the list in place.
- list.copy()
  - Return a shallow copy of the list. Equivalent to a[:].

### 5.1.1. Using Lists as Stacks (“last-in, first-out”)

```bash
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

### 5.1.2. Using Lists as Queues (“first-in, first-out”)

- however, lists are not efficient for this purpose.
  - While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
- To implement a queue, use [collections.deque] which was designed to have fast appends and pops from both ends.

```bash
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

Common applications, assume we want to create a list of squares, like:

```bash
>>> [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

```bash
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

- If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

### 5.1.4. Nested List Comprehensions

```bash
>>> matrix = [[1, 2, 3, 4, 0],[5, 6, 7, 8, 0],[9, 10, 11, 12, 0]]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> [[row[i] for row in matrix] for i in range(5)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12], [0, 0, 0]]
>>> [[row[i] for row in matrix] for i in range(6)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
  File "<stdin>", line 1, in <listcomp>
IndexError: list index out of range
```

In the real world, you should prefer built-in functions to complex flow statements.

```bash
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12), (0, 0, 0)]

```

- zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables.
  - If those values are important, use itertools.zip_longest() instead.
- zip() in conjunction with the `*` operator can be used to unzip a list

## 5.2. The del statement

There is a way to remove an item from a list given its index instead of its value

```bash
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

- Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.
  - on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly
    - Empty tuples are constructed by an empty pair of parentheses
  - A tuple consists of a number of values separated by commas
    - a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses)
- Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

```bash
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

```bash
>>> t = 12345, 54321, 'hello!'
>>> x, y, z = t
```

## 5.4. Sets

- an unordered collection with no duplicate elements.
  - Basic uses include membership testing and eliminating duplicate entries.
  - Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
- Curly braces or the set() function can be used to create sets.
  - Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

```bash
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

Similarly to list comprehensions, set comprehensions are also supported:

```bash
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 5.5. Dictionaries

dictionaries are indexed by keys, which can be any immutable type

```bash
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

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

```bash
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

```bash
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

```bash
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## 5.6. Looping Techniques

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

```bash
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

```bash
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

```bash
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

```bash
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

```bash
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

```bash
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 5.7. More on Conditions

- Note that in Python, unlike C, assignment cannot occur inside expressions.
  - it avoids a common class of problems encountered in C programs: typing `=` in an expression when `==` was intended.
- All comparison operators have the same priority, which is lower than that of all numerical operators.
  - The comparison operators `in` and `not in` check whether a value occurs (does not occur) in a sequence.
  - The operators `is` and `is not` compare whether two objects are really the same object; this only matters for mutable objects like lists.
- the outcome of a comparison (or of any other Boolean expression) may be negated with `not`.
- The Boolean operators `and` and `or` are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.
  - For example, if `A` and `C` are true but `B` is false, `A and B and C` does not evaluate the expression `C`.

## 5.8. Comparing Sequences and Other Types

- The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted.
  - If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively.
  - If all items of two sequences compare equal, the sequences are considered equal.
  - If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one.
  - Lexicographical ordering for strings uses the Unicode code point number to order individual characters.

```bash
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

---

[Data Structures]:https://docs.python.org/3/tutorial/datastructures.html

[collections.deque]:https://docs.python.org/3/library/collections.html#collections.deque
