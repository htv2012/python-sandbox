# Introduction

Sometimes, we have too many tests which we cannot run all of them in
one session. Thus, we would like to run only a portion of them. This
folder represent a solution: We only run, say 30% number of tests at a
time. That 30% amount is in `test_options.json` file.


# Running The Tests

From the terminal, run the test by issuing the following command

    make

Note that each time we run `make`, we see a different set of
tests. Hopefully over time, we will see all of them run.


# How Does It Work?

The magic happens inside the `pytest_collection_modifyitems()` hook.
This hook takes among other parameters the `items`, a list of tests. What
we can do is to delete some tests in this list and the remainder will
be run.

# Roadmap

This algorithm randomly delete tests so `pytest` will not run them. Over
time, we might see some of them got run more than others. To remedy this,
we might want to implement an algorithm which ensure the even distribution
of tests.

ALternatively, we might keep track (in a file, or a database) the last
time a test got run and pick from a list of least-frequently-run tests.

