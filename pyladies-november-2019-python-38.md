# What's New in Python 3.8
## PyLadies November 2019

---

# Links

* https://realpython.com/python38-new-features/ - good overview of what's new in 3.8
* https://docs.python.org/3.8/whatsnew/3.8.html - official what's new, can be hard to read :/

---

# Sidenote: How to Install

* https://github.com/pyenv/pyenv - Install and manage lots of Python versions (version manager)
* https://asdf-vm.com - Even higher level, version manager for version managers (including pyenv)

---

# Walrus Operators (AKA Assignment Expressions)

```python
>>> print(ham := "spam")
spam
>>> ham
'spam'
>>> inputs = list()
>>> while (current := input("Write something: ")) != "quit":
...   inputs.append(current)
...
Write something: Hello
Write something: There
Write something: quit
>>> inputs
['Hello', 'There']
>>>
>>> {input("key: "): input("value: ")}
key: ham
value: spam
{'ham': 'spam'}
```

---

# Position Only Arguments

Mostly of interest to library writers. Big benefit is more explicit args and can rename internally without affecting people's code. Very subtle change.

```python
>>> float(x="1.2")
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: float() takes no keyword arguments
>>> help(float)
    float(x=0, /)
>>> float("1.2")
1.2
```

---

# typing.Literal

--- 

# f-string improvements

```python
>>> x, y, z, a, b, c = range(6)

# old
>>> f"x={x} y={y} z={z} a={a} b={b} c={c}"
'x=0 y=1 z=2 a=3 b=4 c=5'

# new
>>> f"{x=} {y=} {z=} {a=} {b=} {c=}"
'x=0 y=1 z=2 a=3 b=4 c=5'

# with expressions!
>>> print(f'{theta=}  {cos(radians(theta))=:.3f}')
theta=30  cos(radians(theta))=0.866
```

---

# Syntax Warnings as Useful Hints

(I like this trend in languages.)

```python
>>> "a" is "b"
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False

>>> [
... (1,2)
... (3,4)
... ]
# <stdin>:2: SyntaxWarning: 'tuple' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object is not callable
```
