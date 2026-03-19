Given classes such as:

```python
@dataclasses.dataclass(frozen=True)
class User:
    uid: int
    alias: str
    is_admin: bool
    shell: Optional[str] = "bash"
```

We want to instantiate this class using parameters from command
line. The solution is to create a `ClassParamType`, which allow us
to specify from command line as:


```
--user 501,anna,zsh
```

which translates to 

```python
User(uid=501, alias='anna', shell='zsh')
```

