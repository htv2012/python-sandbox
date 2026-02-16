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


@task
def backup(c: Connection, src: str, dest: str):
    src_path = pathlib.Path(src).expanduser().resolve()

    with (
        tempfile.TemporaryDirectory() as temp_dir,
        create_remote_temp_dir(c) as remote_temp_dir,
    ):
        arc = shutil.make_archive(
            base_name=f"{temp_dir}/{src_path.name}",
            format="bztar",
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
