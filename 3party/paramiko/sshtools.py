import pathlib

import paramiko


def parse_config(filename=None):
    config_path = pathlib.Path(filename or "~/.ssh/config").expanduser()
    config = paramiko.SSHConfig.from_path(config_path)
    return config


def connect_with_config(host):
    config = parse_config()
    cfg = config.lookup(host)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(
        cfg["hostname"], username=cfg.get("user"), key_filename=cfg.get("identityfile")
    )
    return client


def open_sftp(
    path: str, *args, mode="r", bufsize=-1, **kwargs
) -> paramiko.sftp_file.SFTPFile:
    """Open a sftp connection.

    :param path: Remote path
    :param args: Additional arguments which will be passed to SSHClient.connect()
    :param mode: Open mode, same as for function open()
    :param bufsize: Buffer size, same as for function open()
    :param kwargs: Additional keyword arguments which will be passed to SSHClient.connect()
    :return: A remote file object
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(*args, **kwargs)
    sftp = client.open_sftp()
    return sftp.file(path, mode, bufsize)
