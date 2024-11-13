def _action_not_allowed(*args, **kwargs):
    raise RuntimeError("Object closed")


def mark_as_closed(obj):
    for name in dir(obj):
        if name.startswith("_"):
            continue
        member = getattr(obj, name)
        if not callable(member):
            continue

        if not getattr(member, "accessible_while_closed", False):
            setattr(obj, name, _action_not_allowed)


def accessible_while_closed(obj):
    obj.accessible_while_closed = True
    return obj
