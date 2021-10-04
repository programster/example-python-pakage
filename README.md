# Example Python Package

An example python package built from watching [this talk](https://blog.programster.org/lecture-publishing-perfect-python-packages-on-pypi#).
and also taking ["How to add additional files to a wheel"](How do you add additional files to a wheel?) into account.
Edit the info in setup.py for the metadata of the package. 
E.g. the package name, description, version etc.


## Installation

You can install using this repository as a URL you pass to pip with (this is assuming you have set up an SSH key with GitHub):

```bash
python3 -m pip install \
  git+ssh://git@github.com:22/programster/example-python-pakage.git@alternative-with-binary-includes
```

If you publish to PyPi, then you would be able to install with:

```bash
python3 -m pip install helloworld
```

## Usage
```python
from britney import run

# Copies britney.jpg file to wherever you are.
run()
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
