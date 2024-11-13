import json
import pathlib

import requests


def get_configuration():
    """
    Retrieves the configurations from a file
    """
    config_filename = pathlib.Path("~/.config/pastebin.json").expanduser()
    if not config_filename.exists():
        config_filename.parent.mkdir(exist_ok=True)
        config_source = pathlib.Path(
            "~/myenv/dotfiles/.config/pastebin.json"
        ).expanduser()
        if config_source.exists():
            config_filename.symlink_to(config_source)
        else:
            raise SystemExit(f"Cannot find configuration file {config_filename}")

    with open(config_filename) as file_handle:
        configuration = json.load(file_handle)

    return configuration


cfg = get_configuration()
print(cfg)

s = requests.Session()
payload = {
    "api_option": "list",
}
payload.update(cfg)
url = "https://pastebin.com/api/api_post.php?api_dev_key=0f5ebdccdc20288d8946008d7bc6fb74&api_user_key=6a314872d831cdcc4d1481202c0666ec&api_option=list"
r = s.post(url)
print(r)
