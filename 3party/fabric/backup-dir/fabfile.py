# fabfile.py
import contextlib
import logging
import os
import pathlib
import shutil
import tempfile

from fabric import Connection, task

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
logger = logging.getLogger(__name__)


@contextlib.contextmanager
def create_remote_temp_dir(c: Connection):
    res = c.run("mktemp -d", hide=True)
    remote_temp_dir = res.stdout.strip()
    logger.info("Remote temp dir: %s", remote_temp_dir)

    yield remote_temp_dir

    c.run(f"rm -fr {remote_temp_dir}", hide=True)


def get_local_tar_formats():
    formats = set(x[0] for x in shutil.get_archive_formats())
    return set(formats)


def get_remote_tar_formats(c: Connection):
    res = c.run("tar --help", hide=True)
    lookup = [
        ("--xz", "xztar"),
        ("--bzip2", "bztar"),
        ("--gzip", "gztar"),
    ]
    formats = set(format for flag, format in lookup if flag in res.stdout)
    formats.add("tar")
    return formats


def get_common_tar_format(c: Connection):
    remote_formats = get_remote_tar_formats(c)
    local_formats = get_local_tar_formats()
    common = remote_formats & local_formats

    for format in ["xztar", "bztar", "gztar", "zip"]:
        if format in common:
            logger.info("Common tar format: %r", format)
            return format

    logger.info("Common tar format: %r", "tar")
    return "tar"


@task
def backup(c: Connection, src: str, dest: str):
    src_path = pathlib.Path(src).expanduser().resolve()

    with (
        tempfile.TemporaryDirectory() as temp_dir,
        create_remote_temp_dir(c) as remote_temp_dir,
    ):
        arc = shutil.make_archive(
            base_name=f"{temp_dir}/{src_path.name}",
            format=get_common_tar_format(c),
            root_dir=str(src_path.parent),
            base_dir=src_path.name,
        )
        logger.info("Archive %s into %s", src_path, arc)

        c.put(arc, remote=remote_temp_dir)

        remote_arc = str(pathlib.Path(remote_temp_dir) / pathlib.Path(arc).name)
        logger.info("Remote archive: %s:%s", c.original_host, remote_arc)

        c.run(f"mkdir -p {dest}", hide=True)
        with c.cd(dest):
            c.run(f"tar xf {remote_arc}", hide=True)

        print(f"{src} -> {c.original_host}:{dest}")
