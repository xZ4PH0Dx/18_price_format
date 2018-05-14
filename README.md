# Price Formatter

This program formats float price.

# How to run
Example of running a script on a Linux with a Python3 interpreter.
```bash
$python3 format_price.py 1245623.577
1 245 623.58
```
Also you can user this program as a module:
```python
from format_price import format_price

format_price(12345.324)
```
Will output
```python
12 345.32
```

# How to run test
```bash
$python -m unittest tests.py
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
