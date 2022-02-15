import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pdfid",
    version="1.1.0",
    description="PDFID simple tool to analyze PDF malicious files by DidierStevens. Customized by Matteo Lodi to be used as a library.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mlodic/pdfid",
    author="Matteo Lodi",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    packages=["pdfid"],
    python_requires=">=2.6, <4",
    include_package_data=True,
    install_requires=[],
)
