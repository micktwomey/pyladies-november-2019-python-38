import typing

class HamDict(typing.TypedDict):
    ham: str
    spam: int
    eggs: float

x: HamDict = {"ham": "spam", "spam": "13", "eggs": 1.2}
print(x)
y: HamDict = {"ham": 12, "eggs": "spam"}
print(y)
