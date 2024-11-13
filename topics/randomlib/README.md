# Overview
This library provide functions for generating random names which
can be used in applications and in testing.

# Random Names Generator


```python
>>> import randomlib

>>> # 1 name
>>> randomlib.generate_name()
'frugal-perch'

>>> # 1 name, in a list
>>> randomlib.generate_names()
'silent-prawn'

>>> # 3 names
>>> randomlib.generate_names(3)
['wilted-quail', 'noisy-cattle', 'impractical-armadillo']

>>> # Customize the separator
>>> randomlib.generate_names(separator=".")
['oblong.bean']

>>> # Add prefix, suffix
>>>  randomlib.generate_names(prefix="www.", suffix=".com")
['www.imperfect-bedbug.com']

>>> # Limit the overall length
>>> randomlib.generate_names(max_length=10)
['palatable-']

>>> # Limit the overall length, including prefix and suffix
>>> randomlib.generate_names(prefix="www.", suffix=".com", max_length=16)
['www.loathsom.com']
```

# Random URIs Generator

```python
>>> randomlib.generate_uri()  # 1 URI
'http://masculine-buzzard.com'

>>> randomlib.generate_uris(3)  # 3 URIs
['http://stingy-marten.com',
 'http://insecure-anaconda.com',
 'http://noxious-viper.com']

>>> randomlib.generate_uris(count=2, protocol="https", domain=".net")  # Customize
['https://experienced-impala.net', 'https://vapid-morel.net']
```

# Random Email Generator

```python
>>> randomlib.generate_email()  # 1 email address
'considerate@sycamore.com'

>>> randomlib.generate_emails(count=2)  # 2 email addresses
['worried@stickweed.com', 'bad@gayal.com']

>>> randomlib.generate_emails(count=2, domain=".biz")  # Customize
['disgusting@pinniped.biz', 'heartfelt@shadbush.biz']
```

# Random location (Path) Generator

```python
>>> randomlib.generate_location()  # For testing
'/electric-haddock'

>>> randomlib.generate_locations(3)  # Multiple locations
['/worst-strawberry', '/impassioned-marina', '/calculating-rapeseed']
```

