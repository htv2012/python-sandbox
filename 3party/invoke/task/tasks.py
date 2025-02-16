import contextlib

from invoke import task


def show_obj(obj):
    names = [name for name in sorted(dir(obj)) if not name.startswith("_")]
    for name in names:
        attribute = getattr(obj, name)
        if callable(attribute):
            print(f"- {name}()")
            with contextlib.suppress(AttributeError):
                print(f"  {attribute.__doc__.strip().splitlines()[0]}")
        else:
            print(f"- {name}: {attribute!r}")


@task
def show_context(c):
    show_obj(c)


@task
def show_result(c):
    result = c.run("pwd", hide=True)
    show_obj(result)
