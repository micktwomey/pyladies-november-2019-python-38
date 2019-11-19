import typing

def ham(spam: typing.Literal["spam", "eggs"]) -> str:
    return spam

x = ham("cheese")
print(x)
