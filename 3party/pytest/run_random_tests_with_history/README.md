# Introduction

Sometimes, we have tests which take a long time to run (in this case,
they are marked with the `long` marker) and don't have time to run all
of them in a session. This directory provides a solution: Run only a
small number of long tests per session.

# How to Run Tests

From the terminal, issue the following command:

    make

Notes

- Tests without the `long` marker will always get run
- Tests with the `long` marker are run only 10 tests per session.
- This value 10 is in the test_options.json file, which we can adjust

# How Does It Work?

The magic is in the `pytest_collection_modifyitems()` hook. Among
other parameters, it takes in `items` which is a list of tests. In this
function, we will randomly mark some tests with the skip marker. The
hook also maintain a hidden file, `.tested.csv` to keep track of those
test we ran so far and skip those as well. When we run all the tests,
we reset the `.tested.csv` file (by emptying it) and start over again.

