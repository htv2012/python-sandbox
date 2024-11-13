import inspect
import io
import reprlib

from fabric import Connection, task


def show_obj(obj, label: str, reference_url: str):
    names = sorted(name for name in dir(obj) if not name.startswith("_"))
    divider = "-" * 72
    print()
    print(divider)
    print()
    print(f"# The {label} Object")

    print("\n## General")
    print(f"- Reference: {reference_url}")
    print(f"- repr: {reprlib.repr(obj)}")
    print("- Method resolution order:")
    for klass in obj.__class__.__mro__:
        print(f"  - {klass!r}")

    methods = io.StringIO()

    print("\n## Attributes")
    for name in names:
        attribute = getattr(obj, name)
        if callable(attribute):
            signature = inspect.signature(attribute)
            methods.write(f"\n- {name}{signature}\n")
            docstr = attribute.__doc__
            if docstr:
                first_line = docstr.strip().splitlines()[0]
                methods.write(f"  {first_line}\n")
        else:
            print(f"- {name} = {reprlib.repr(attribute)}")

    print("\n## Methods")
    print(methods.getvalue())


@task()
def introspection(conn: Connection):
    result = conn.run("whoami", hide=True)
    show_obj(
        obj=conn.config,
        label="Config",
        reference_url="https://docs.fabfile.org/en/latest/api/config.html",
    )
    show_obj(
        obj=conn,
        label="Connection",
        reference_url="https://docs.fabfile.org/en/latest/api/connection.html",
    )
    show_obj(
        obj=result,
        label="Result",
        reference_url="https://docs.fabfile.org/en/latest/api/runners.html",
    )
