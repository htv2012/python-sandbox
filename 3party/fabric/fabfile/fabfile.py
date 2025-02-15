import csv

from fabric import Connection, task


def get_os_release(conn: Connection):
    result = conn.run("cat /etc/os-release", hide=True)
    dialect = csv.Sniffer().sniff(result.stdout)
    reader = csv.reader(result.stdout.splitlines(), dialect=dialect)
    os_release_info = dict(reader)
    return os_release_info


def get_update(os_release_info: dict):
    os_id = os_release_info.get("ID_LIKE")
    if os_id == "debian":
        return "apt update", "apt upgrade -y", "apt install -y"
    raise ValueError(f"Do not handle {os_id}")


@task
def adduser(conn: Connection, user="haiv"):
    """Add a new user"""
    conn.sudo(f"adduser --ingroup sudo {user}")
    conn.sudo(f"mkdir ~{user}/.ssh")
    conn.sudo(f"cp ~/.ssh/authorized_keys ~{user}/.ssh")
    conn.sudo(f"chmod 600 ~{user}/.ssh/authorized_keys")
    conn.sudo(f"chown --recursive {user}:sudo ~{user}/.ssh")


@task
def apt_update(conn: Connection):
    """Run apt update && apt-upgrade -y"""
    conn.sudo("apt update")
    conn.sudo("yes | apt upgrade -y")


@task(apt_update)
def install_packages(conn: Connection):
    """Initial install of Ubuntu packages"""
    osr = get_os_release(conn)
    _, _, install = get_update(osr)
    conn.sudo(f"{install} fzf git openssh-server ripgrep stow vim zsh")


@task
def info(conn: Connection):
    print("Host Name:      ", end="")
    conn.run("hostname")

    print("Uptime:        ", end="")
    conn.run("uptime")


    print("Python version: ", end="")
    conn.run("python3 --version")

    conn.run("lsb_release -a")


    print("-" * 80)

