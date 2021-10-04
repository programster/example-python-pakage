# Sript for building our package.
# Run with: python3 setup.py bdist_wheel

from setuptools import setup

# Specify the version for the package. This is at the top as you are likly
# to change it the most frequently (bump up the version)
version = '0.0.1'


# Specify the name for the package.
packageName = 'britney'


# Give a description for the package.
packageDescription = "This is an example python package."


# Specify the author details for the package.
authorName="Programster"
authorEmail="noreply@programster.org"


# Specify a URL for the package. Preferably where the source code is. E.g. Github.
url="https://github.com/programster/example-python-pakage"


# Specify any requirements here. E.g. "blessings ~= 1.7"
requirements = []


# Specify any dependencies required for developing this package.
# better to use this than to use requirements.txt 
# https://youtu.be/GIF3LaRqgXo?t=1089
devDependencies = [
    "pytest>=3.7"
]


# Specify the classifiers. More info here: https://pypi.org/classifiers/
# Code uses an f string which requires 3.6+
classifiers = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]


with open("README.md", "r") as fh:
    longDescription = fh.read()


setup(
    name = packageName,
    version = version,
    description = packageDescription,
    long_description=longDescription,
    long_description_content_type="text/markdown",
    author=authorName,
    author_email=authorEmail,
    url=url,
    packages = ["britney"],
    package_dir = {"britney" : "src"},
    package_data = {
        'britney': ["data/*.jpg"],
    },
    classifiers = classifiers,
    install_requires = requirements,
    extras_require = {
        "dev": devDependencies
    },
    zip_safe=False,
    include_package_data=True
)
