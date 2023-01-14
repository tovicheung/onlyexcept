# onlyexcept
Want to only catch a specific type of exception, and not its subclasses? Use `onlyexcept`!

## Installation
`pip install onlyexcept`

## Usage
Normal
```py
try:
    raise ValueError
except Exception:
    print("caught")
# ValueError will be caught as it is a subclass of Exception
```

Using onlyexcept
```py
from onlyexcept import Only
try:
    raise ValueError
except Only(Exception):
    print("caught")
# ValueError will not be caught as it is not Exception
```
