# Serial Text Bump

Given a string such as 'edit 26', I often need to increase the embedded number and return a new string, 'edit 27'. The `serial` module will do that.

## Usage

```python
>>> from hvtext.serial import bump

>>> bump('edit 26')
'edit 27'

>>> bump('edit 26', -5)
'edit 21'
```

## Command-Line Usage

```bash
$ python3 -m hvtext.serial 'edit 26'       # Increase by 1
edit 27

$ python3 -m hvtext.serial 'edit 26' -i 5  # Increase by 5
edit 27

$ python3 -m hvtext.serial 'edit 26' -d 5  # Decrease by 5
edit 21
```
