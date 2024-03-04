# Snirk Release Process

Currently Snirk is manually released and published to [PyPI][pypi] by a repo maintainer.

## releasing

The [poetry-bumpversion][poetry-bumpversion] plugin is used to update the version before publishing.

After the version is updated, and the release is built, it can be [published with poetry][poetry-publish].

The release workflow follows:

* Use `poetry version` to bump version
* Update `CHANGELOG.md`
* Create and merge pull request off release branch
* Create Github Release / tag for new version
* Checkout updated `main` after PR merges
* Build with `poetry build`
* Publish to PyPI with `poetry publish`

### publishing docs

The GitHub Actions workflow at `.github/workflows/push-mkdocs-deploy.yaml` is run when a PR is merged to `main`
which builds and publishes documentation to [github pages][gh-pages] using [`mkdocs`][mkdocs] via running
the script at `tools/publish-mkdocs.sh`.

[gh-pages]: https://coffeemancy.github.io/snirk
[mkdocs]: https://www.mkdocs.org
[poetry-bumpversion]: https://github.com/monim67/poetry-bumpversion
[poetry-publish]: https://python-poetry.org/docs/cli/#publish
[pypi]: https://pypi.org/project/snirk
