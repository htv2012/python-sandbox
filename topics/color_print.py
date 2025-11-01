import re

COLOR = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    "reset": "\033[0m"
}

pat = re.compile(r"<<\s*(\w+)\s*(.+?)\s*?>>")

def apply_color(matched: re.Match):
    fg = matched[1]
    text = matched[2]
    return f"{COLOR[fg]}{text}{COLOR['reset']}"

def cprint(text: str, sep=' ', end='\n', file=None, flush=False):
    text = pat.sub(apply_color, text)
    print(text, sep=sep, end=end, file=file, flush=flush)

cprint("I like <<red roses>>, <<blue violets>>, and <<yellow carnations>>.")