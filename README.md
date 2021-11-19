# Testing with PyTest

The standard Python installation alone offers several options such as the `doctest`, `unittest`, and `test` modules. The `doctest` module allows you to combine tests with example documentation. The `unittest` module allows you to easily write regression tests. The `test` module is meant for internal usage only, so unless you are planning to modify the Python core, you probably won't need this one.

The `pytest` module has roughly the same purpose as the `unittest` module, but it's much more convenient to use and has a few extra options.

## Semaphore tutorial

This repository follows the introduction to `pytest` on
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

It shows the basic usage of `pytest`, `pytest fixtures` and `parametrized test functions`.

The files `wallet.py`, `test_wallet.py` and `test_capitalize` come from this tutorial.

## Packt Mastering Python (2016) - Chapter 10

Running doctests with `pytest`

```sh
    pytest --doctest-modules -v square-doctest.py
```

### conftest.py

`conftest.py` is a special file for `pytest` that can be used to override or extend `pytest`. This file will automatically be loaded by every test run in that directory.

### Automatic arguments using fixtures

The fixture system of `pytest` magically executes a fixture function with the same name as your arguments. Because of this, the naming of the arguments becomes very important, as they can easily collide with other fixtures. To prevent collisions, the scope is set to `function` by default. However, `class`, `module`, and `session` are also valid options for the scope.

There are several fixtures available by default, some of which you will use often, and others most likely never. The following command shows a complete list of them.

```shell
   pytest --fixtures
```

In most projects, you will need to create your own fixtures to make things easier. Fixtures make it trivial to repeat code that is needed more often. Fixtures are similar to regular functions, context wrappers, etc. but the special thing about fixtures is that they themselves can accept fixtures as well. If your function needs the pytestconfig variables, it can ask for it without needing to modify the calling functions.

### Tip for fixtures

    $ pytest --fixtures

(Shows all available fixtures)

### coverage

```python
    pytest test_cube.py --cov-report=html --cov-report=term-missing --cov=cube
```

### Run CI as github actions

Following:

https://www.techiediaries.com/python-unit-tests-github-actions/


### Improvements
