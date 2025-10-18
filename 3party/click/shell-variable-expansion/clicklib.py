import os



def expand_shell_vars(text: str) -> str:
    text = text.replace("~", "${HOME}")
    text = os.path.expanduser(text)
    text = os.path.expandvars(text)
    return text


def expand_shell_vars_callback(ctx, param, value):
    print(f"Before expansion, {value = }")
    value = expand_shell_vars(value)
    print(f"After expansion, {value = }")
    return value
