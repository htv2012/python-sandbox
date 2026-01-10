#!/usr/bin/env python3
from invoke import task


@task
def format(c):
    print("format")


@task()
def lint(c):
    print("lint")


@task(pre=[format, lint])
def build(c):
    print("build")


@task(pre=[build])
def test(c):
    print("test")


@task(pre=[format])
def release(c):
    print("release")
