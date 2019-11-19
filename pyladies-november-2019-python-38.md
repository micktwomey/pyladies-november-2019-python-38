# What's New in Python 3.8
## PyLadies November 2019

---

# Language changes

- walrus operators
- position only parameters
- f-strings support = for self-documenting expressions and debugging

---

# Library changes

- typing
    - Literal types
    - Typed dictionaries
    - Final objects
    - Protocols
- importlib.metadata
- math
- statistics
- multiprocessing.shared_memory

---

# C and CPython changes

- Parallel filesystem cache for compiled bytecode files
- Debug build uses the same ABI as release build
- PEP 578: Python Runtime Audit Hooks
- PEP 587: Python Initialization Configuration
- Vectorcall: a fast calling protocol for CPython
- Pickle protocol 5 with out-of-band data buffers
- SyntaxWarnings for potential mistakes
- Lotsa speed improvements

---

# Governence changes

- Python Steering Council
    - Barry Warsaw
    - Brett Cannon
    - Carol Willing
    - Guido van Rossum
    - Nick Coghlan

---

# Links

* https://realpython.com/python38-new-features/ - good overview of what's new in 3.8
* https://docs.python.org/3.8/whatsnew/3.8.html - official what's new, can be hard to read (something cool might be a bullet point).

---

# Sidenote: How to Install

* Official installers
* https://github.com/pyenv/pyenv - Install and manage lots of Python versions (version manager)
* https://asdf-vm.com - Even higher level, version manager for version managers (including pyenv)
* Anaconda: `conda create -n py38 python=3.8`

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

```python
import typing

def ham(spam: typing.Literal["spam", "eggs"]) -> str:
    return spam

x = ham("cheese")
print(x)
```

```sh
$ python typing_literal.py
cheese

$ mypy typing_literal.py
typing_literal.py:6: error: Argument 1 to "ham" has incompatible type \
"Literal['cheese']"; expected "Union[Literal['spam'], Literal['eggs']]"
Found 1 error in 1 file (checked 1 source file)
```

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


---

# @functools.cached_property

```python
import functools
import statistics

class Dataset:
    def __init__(self, sequence_of_numbers):
        self.data = sequence_of_numbers
 
    @functools.cached_property
    def variance(self):
        return statistics.variance(self.data)
 
    @property
    def boring_variance(self):
        if not hasattr(self, "_cached_variance"):
            self._cached_variance = statistics.variance(self.data)
        return self._cached_variance
```

^ Super useful way to speed up stuff which is only *computed once*

---

# json.tool --json-lines

```sh
$ cat /tmp/foo.jsons
{"1":2}
{"3":4}
{"5":6}

$ python -m json.tool --json-lines /tmp/foo.jsons
{
    "1": 2
}
{
    "3": 4
}
{
    "5": 6
}
```

(You probably want to use `jq . /tmp/foo.jsons` instead though.)

^ Very handy for JSON encoded logs, one per line

---

# asyncio repl

```python
$ python -m asyncio
asyncio REPL 3.8.0 (default, Oct 15 2019, 15:14:34)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result="hello there")
'hello there'
```

---

# Happy Eyeballs

:laughing: :eyes:

asyncio now implements Happy Eyeballs (connect to both IPv4 and IPv6 and use whichever responds faster).

(Only included in slides so I could say Happy Eyeballs.)

---

# logging force flag

Solves a really, really annoying problem.

```python
>>> import logging
>>> logging.basicConfig(level=logging.WARNING)
>>> logging.info("foo")
# no info message as expected
>>> logging.basicConfig(level=logging.INFO)
>>> logging.info("foo")
# where's my info log message?
>>> logging.basicConfig(level=logging.INFO, force=True)
>>> logging.info("foo")
INFO:root:foo
# yay!
```

:rainbow:  `pip install coloredlogs` then use `coloredlogs.install()`
