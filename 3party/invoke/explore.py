import contextlib
import reprlib


def show_obj(obj):
    print(f"- type: {obj.__class__}")
    names = [name for name in sorted(dir(obj)) if not name.startswith("_")]
    for name in names:
        attribute = getattr(obj, name)
        if callable(attribute):
            print(f"- {name}()")
            with contextlib.suppress(AttributeError):
                print(f"  {attribute.__doc__.strip().splitlines()[0]}")
        else:
            print(f"- {name}: {reprlib.repr(attribute)}")
