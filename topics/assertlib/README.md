```python
verify(myvar).eq("hello")
verify(count).lt(10)
verify(count).ge(5)
verify("foo").in_(["foo", "bar"])
verify(mylist).contains("foo")
verify(mylist).has_length(3)

msg("name is required").verify(name).not_none()
```