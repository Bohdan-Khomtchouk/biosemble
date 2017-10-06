#!/usr/bin/env python

# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------

from distutils.core import setup
from Cython.Build import cythonize

setup(name='general',
      ext_modules=cythonize("general.pyx"),)
