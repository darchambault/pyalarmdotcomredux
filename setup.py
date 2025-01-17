import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read("README.md")

setup(
    name="pyalarmdotcomredux",
    version="0.2.2",
    url="http://github.com/darchambault/pyalarmdotcomredux/",
    license=" ",
    author="Dominique Archambault",
    install_requires=["bs4", "aiohttp>=3.8.0"],
    author_email="1649005+darchambault@users.noreply.github.com",
    description="Python Interface for Alarm.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pyalarmdotcomredux"],
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
