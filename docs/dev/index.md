# Snirk Developer Docs

Development is intended to be done in a python3.11+ virtualenv with [`poetry`][poetry].

To get started, clone this repository, create and use a virtualenv, and install dependencies with `poetry`:

```bash
cd snirk
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
poetry install
```

!!! tip

    You can use a different path for your venv if desired. It doesn't have to be `.venv`.

## development and contributions overview

Snirk uses several tools as part of the development stack.

* [`poetry`][poetry]: packaging and dependency management
* [`black`][black]: consistent code formatting
* [`flake8`][flake8]: code error/quality checking
* [`isort`][isort]: consistent import sorter
* [`mypy`][mypy]: type-checking
* [`mkdocs`][mkdocs]: documentation generation
* [`pytest`][pytest]: unit-testing

All of the above tools are installed as developer dependencies when `poetry install` is run.

Testing is intended to be able to be done locally, but tests are also run as part of a github workflow.

Additional checks are run as part of a github workflow. This includes tools which are not `python` and thus not
included in developer dependencies:

* [`markdownlint-cli`][markdownlint]: error/quality checking of markdown files (e.g. documentation)
* [`shellcheck`][shellcheck]: error/quality checking of shell files

### contribution workflow

The recommended approach for making contributions follows:

* Assure all local tests work before making changes
* Make changes, run local tests, and iterate
* Commit changes to your own fork/branch
* Open a Pull Request (PR) on github.com from your fork/branch to snirk repo
* Verify that remote github workflow tests pass
* Mark PR as "Ready for Review"
* Receive review and iterate on any requested changes
* PR is merged by repo maintainers

## testing

The testing stragegy follows:

* Catch syntax issues and common "gotchas" via code formatters (`black`) and linters (`flake8`)
* Use `mypy` type-checking to catch many possible problems and boundary issues
* Unit testing via `pytest` for snirk-specific logic (e.g. filtering finding devices, checking device capabilities)
* Runnable `examples/`  to interact with actual SNI server and devices (e.g. Fx Pak Pro, Retroarch)

### local testing

An example [`git` pre-commit hook][git-pre-commit] script is included which can be used to automate local testing. If
installed, it will be run before a commit can be made.

To install the script, make a copy:

```bash
cp tools/pre-commit.sh .git/hooks/pre-commit
```

!!! note

    If your virtualenv is not ".venv", then the copied pre-commit hook script will need to be modified to use
    your venv.

This will run all testing tools which are part of the development stack. It will also run additional tools which are
not included in the developer stack but are run as part of a github workflow, if they are available.

!!! tip

    The pre-commit script can be run at any time, although it will run automatically when `git commit` is attempted.
    If you want to run it without committing you can just run `.git/hooks/pre-commit`.

Example output of the pre-commit script:

```raw
black ✔
isort ✔
flake8 ✔
mypy ✔
markdownlint ✔
mkdocs ✔
shellcheck  ✔
pytest (Python 3.11.7) ✔
```

### unit testing

Most of the code in this repo involves wrapping communication to devices with SNI. As such, unit testing coverage
via `pytest` is limited, requiring mocking of SNI gRPC calls. Currently, there is around 44% coverage. Tests are
included in the `tests/` directory.

The [pytest-asyncio plugin for `pytest`][pytest-asyncio] is used which adds support for testing `asyncio` coroutines.

### running examples

There are example scripts included in the `examples/` directory (explained in [usage][usage]).

These can be run locally and are expected to work, but require actual devices (FxPak Pro, RetroArch, etc.), as well
as running [sni][sni].

As such, they are not really amendable to being run as part of a CI workflow, and instead will need to be checked
manually when possible. This may mean some future changes would require repo maintainers or other code reviewers to
manually check certain changes on PRs, if the code authors are unable to test.

## building

Snirk can be built with `poetry`:

```bash
poetry build
```

This will create a sdist source tarball and wheel in the `dist/` directory. The wheel should be installable
in another virtualenv and acts as the final artifact. These are what are uploaded to [PyPI][pypi].

### building and serving docs

Snirk uses [`mkdocs`][mkdocs] for building documentation.

Docs can be built via:

```bash
mkdocs build
```

Additionally, a local docs server can be spun up and then tested in browser (default binds to `localhost:8000`):

```bash
mkdocs serve
```

## additional developer details

* [Release process][release-process]
* [SNI gRPC code generation][sni-grpc-codegen]

[black]: https://github.com/psf/black
[flake8]: https://github.com/pycqa/flake8
[git-pre-commit]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
[isort]: https://pycqa.github.io/isort
[markdownlint]: https://github.com/igorshubovych/markdownlint-cli
[mkdocs]: https://www.mkdocs.org
[mypy]: https://www.mypy-lang.org
[poetry]: https://python-poetry.org
[pypi]: https://pypi.org/project/snirk
[pytest]: https://docs.pytest.org/en/8.0.x
[pytest-asyncio]: https://pytest-asyncio.readthedocs.io
[release-process]: release-process.md
[shellcheck]: https://github.com/koalaman/shellcheck
[sni-grpc-codegen]: sni-grpc-codegen.md
[sni]: https://github.com/alttpo/sni
[usage]: ../usage.md
