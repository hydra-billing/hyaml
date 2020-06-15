# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hyaml",
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version="0.1.6",
    description="HYAML is a one-liner oriented language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/latera/hyaml",
    author="Hydra Billing Solutions",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Pytest",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="antlr language one-liner hydra hyaml",
    packages=find_packages(exclude=["tests"]),
    install_requires=["antlr4-python3-runtime>=4.7.1"],
    extras_require={"dev": ["black", "unittest-xml-reporting", "coverage"]},
    entry_points={"console_scripts": ["hyaml=hyaml:main"]},
    project_urls={
        "Bug Reports": "https://github.com/latera/hyaml/issues",
        "Source": "https://github.com/latera/hyaml",
    },
)
