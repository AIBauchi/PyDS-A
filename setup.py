from setuptools import setup, find_packages

# Package metadata
NAME = "PyDS-A"
VERSION = "1.0.0"
DESCRIPTION = "A collection of data structures and algorithms in Python."
AUTHOR = "Tinny-Robot"
EMAIL = "handanfoun@gmail.com"
URL = "https://github.com/AIBauchi/PyDS-A"
LICENSE = "MIT"
CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Software Development :: Libraries",
]

# Package dependencies
INSTALL_REQUIRES = []

# Package setup
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
)
