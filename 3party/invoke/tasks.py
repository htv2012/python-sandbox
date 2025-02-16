from invoke import task


@task
def apt_update(c):
    c.run("sudo apt update")


@task(pre=[apt_update])
def apt_upgrade(c):
    print("apt-upgrade")
