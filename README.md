# snirk

Snirk is a python wrapper for [SNES Interface gRPC API (SNI)][sni] providing typed asynchronous interfaces for
communicating with SNI-compatible devices (e.g. RetroArch, FxPak Pro).

It is intended to be used as a library by other python tools or applications using SNI.

## installation

Stable releases are available on [PyPI][pypi] and can be installed via typical means, e.g. `pip`:

```bash
pip install snirk
```

## usage

Usage and code examples are provided in [documentation][docs-site].

## development

Development is intended to be done in a python3.11+ virtualenv with [`poetry`][poetry], with [`mypy`][mypy] for
type-checking and [`black`][black] for code formatting. Contributions via Pull Request from your tested fork
are welcome and encouraged!

Additional development and contribution details are provided in [developer documentation][dev docs].

[black]: https://pypi.org/project/black
[docs-site]: https://coffeemancy.github.io/snirk
[dev docs]: https://coffeemancy.github.io/snirk
[mypy]: https://www.mypy-lang.org
[poetry]: https://python-poetry.org
[pypi]: https://pypi.org/project/snirk
[sni]: https://github.com/alttpo/sni
