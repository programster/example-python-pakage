# Example Python Package

An example python package built from watching [this talk](https://blog.programster.org/lecture-publishing-perfect-python-packages-on-pypi#).

Edit the info in setup.py for the metadata of the package. 
E.g. the package name, description, version etc.


## Installation

```bash
pip install helloworld
```

## Usage
```python
from helloworld import sayHello

# Generate "Hello world!"
sayHello()

# Generate "Hello, Bob!"
sayHello("Bob")
```


## Development

Build the package with:

```bash
python3 setup.py bdist_wheel
```

After building, install the package by linking to this file with deve dependencies:

```bash
pip install -e .[dev]
```
