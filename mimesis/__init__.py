# -*- coding: utf-8 -*-

"""Mimesis is a Python library, which helps generate fake data.

Copyright (c) 2016 - 2021 Isaak Uchakaev (Likid Geimfari).
Website: https://mimesis.name
Email: <likid.geimfari@gmail.com>
Repository: https://github.com/lk-geimfari/mimesis
"""

from mimesis.schema import Field, Schema

from .providers import (
    Address,
    BaseDataProvider,
    BaseProvider,
    BinaryFile,
    Choice,
    Choices,
    Code,
    Cryptographic,
    Datetime,
    Development,
    File,
    Finance,
    Food,
    Generic,
    Hardware,
    Internet,
    Numeric,
    Path,
    Payment,
    Person,
    Science,
    Text,
    Transport,
)

__all__ = [
    "Address",
    "BaseDataProvider",
    "BaseProvider",
    "BinaryFile",
    "Finance",
    "Code",
    "Choice",
    "Choices",
    "Datetime",
    "Development",
    "File",
    "Food",
    "Hardware",
    "Internet",
    "Numeric",
    "Path",
    "Payment",
    "Person",
    "Science",
    "Text",
    "Transport",
    "Cryptographic",
    # Has all:
    "Generic",
    # Schema:
    "Field",
    "Schema",
    # Meta:
    "__version__",
    "__title__",
    "__description__",
    "__url__",
    "__author__",
    "__author_email__",
    "__license__",
]

__version__ = "5.0.0"
__title__ = "mimesis"
__description__ = "Mimesis: fake data generator."
__url__ = "https://github.com/lk-geimfari/mimesis"
__author__ = "Isaak Uchakaev (Likid Geimfari)"
__author_email__ = "likid.geimfari@gmail.com"
__license__ = "MIT License"
